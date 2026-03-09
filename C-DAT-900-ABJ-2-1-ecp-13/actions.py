import os
import json
import logging
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv
from openai import OpenAI
import sqlite3
import numpy as np

load_dotenv()
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

DB_PATH = os.getenv("PRODUCT_DB_PATH", "./product_embeddings.db")


def cosine_similarity(a: List[float], b: List[float]) -> float:
    a = np.array(a)
    b = np.array(b)
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def retrieve_similar_products(query_embedding: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT id, sku, title, price, short_desc, embedding FROM products")
        rows = cur.fetchall()
        conn.close()
    except sqlite3.OperationalError:
        logger.error(f"Erreur: Impossible d'ouvrir la base de données à {DB_PATH}.")
        return [] 
        
    results = []
    for r in rows:
        pid, sku, title, price, short_desc, emb_json = r
        try:
            emb = json.loads(emb_json)
        except Exception:
            continue
        score = cosine_similarity(query_embedding, emb)
        results.append({"id": pid, "sku": sku, "title": title, "price": price, "short_desc": short_desc, "score": score})

    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results[:top_k]


class ActionGPTResponse(Action):
    """Action principale pour la recherche sémantique RAG."""
    def name(self) -> Text:
        return "action_gpt_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[SlotSet]:
        user_msg = tracker.latest_message.get("text")
        intent = tracker.latest_message.get("intent", {}).get("name", "")
        
        try:
            emb_resp = client.embeddings.create(model="text-embedding-3-small", input=user_msg)
            user_emb = emb_resp.data[0].embedding
        except Exception as e:
            logger.exception("Embedding creation failed")
            user_emb = []

        top_products = retrieve_similar_products(user_emb, top_k=4) if user_emb else []

        if not top_products:
             answer = "Je n'ai pas trouvé de produits exacts. Pourriez-vous reformuler ou me donner le nom de la marque ?"
             dispatcher.utter_message(text=answer)
             return []

        product_context = "\n".join([f"- {p['title']} | SKU:{p['sku']} | Prix:{p['price']} | {p['short_desc']}" for p in top_products])
        
        prompt = (
            "Tu es un conseiller commercial expert.\n"
            "TA MISSION: Proposer 3 produits pertinents basés sur le contexte ci-dessous.\n\n"
            "FORMAT DE RÉPONSE OBLIGATOIRE (Liste à puces):\n"
            "1. *[Nom du Produit]*\n"
            "   - 💰 Prix: [Prix] FCFA\n"
            "   - 🏷️ SKU: [Code SKU exact]\n"
            "   - 📝 [Phrase courte d'argumentaire]\n\n"
            "RÈGLES:\n"
            "- Tu DOIS afficher le SKU pour chaque produit.\n"
            "- Termine par: 'Souhaites-tu que je réserve l'un de ces produits ?'\n\n"
            f"CONTEXTE PRODUIT:\n{product_context}\n\n"
            f"DEMANDE CLIENT: {user_msg}\n"
            "RÉPONSE:"
        )
        
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=450,
                temperature=0.25,
            )
            answer = completion.choices[0].message.content.strip() 
            
        except Exception as e:
            logger.exception("OpenAI request failed")
            answer = "Désolé, le service de recommandation est indisponible."

        dispatcher.utter_message(text=answer)
        
        shown_ids = [p['id'] for p in top_products]
        return [SlotSet("last_shown_products", json.dumps(shown_ids))]

class ActionHandleOrder(Action):
    """Gère l'étape de confirmation et lance la demande de SKU."""
    def name(self) -> Text:
        return "action_handle_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[SlotSet]:
        product_name_entity = next(tracker.get_latest_entity_values("product_name"), None)
        last_shown_products_json = tracker.get_slot("last_shown_products")
        
        if product_name_entity:
            dispatcher.utter_message(text=f"Excellent choix : {product_name_entity}.")
            dispatcher.utter_message(response="utter_checkout_prompt") 
            return [SlotSet("selected_product_name", product_name_entity)]
        
        elif last_shown_products_json:
            dispatcher.utter_message(response="utter_checkout_prompt") 
            return [] 

        else:
            dispatcher.utter_message(text="Je suis prêt à prendre votre commande ! Quel est le nom ou le SKU du produit ?")
            return []

class ActionShowProduct(Action):
    """Affiche les détails d'un produit par SKU."""
    def name(self) -> Text:
        return "action_show_product"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[SlotSet]:
        sku = next((ent['value'] for ent in tracker.latest_message.get('entities', []) if ent['entity']=='sku'), None)
        
        if not sku:
            user_text = tracker.latest_message.get("text", "").strip()
            if "REF-" in user_text: 
                sku = user_text
        
        if not sku:
            dispatcher.utter_message(text="Je n'ai pas bien saisi le code SKU. Il commence généralement par 'REF-'.")
            return []
            
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        try:
            cur.execute("SELECT title, price, long_desc FROM products WHERE sku LIKE ?", (f"%{sku}%",))
            row = cur.fetchone()
            conn.close()
            
            if not row:
                dispatcher.utter_message(text=f"Je ne trouve pas le produit avec le code {sku}. Vérifiez la référence.")
                return []
                
            title, price, long_desc = row
            dispatcher.utter_message(text=f"✅ **Commande Validée**\n\n📦 Produit: {title}\n💰 Prix: {price} FCFA\n📝 Détails: {long_desc}\n\nPassons au paiement !")
            return [SlotSet("selected_sku", sku)]
            
        except sqlite3.OperationalError:
             dispatcher.utter_message(text="Erreur technique base de données.")
             return []