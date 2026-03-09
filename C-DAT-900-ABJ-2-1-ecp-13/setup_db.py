import os
import json
import sqlite3
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict, Any 

# --- Configuration ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY non trouvée. Assurez-vous d'avoir un fichier .env.")

client = OpenAI(api_key=OPENAI_API_KEY)
DB_PATH = "product_embeddings.db"
JSON_FILE = "products.json"
EMBEDDING_MODEL = "text-embedding-3-small"
# --- Fin Configuration ---

def create_db_and_table(conn):
    """Crée la table des produits si elle n'existe pas."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            sku TEXT,
            title TEXT,
            price REAL,
            short_desc TEXT,
            long_desc TEXT,
            embedding TEXT  -- Stocké comme chaîne JSON
        )
    """)
    conn.commit()

def generate_embedding(text: str) -> List[float]:
    """Génère l'embedding via l'API OpenAI."""
    try:
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Erreur lors de la création de l'embedding: {e}")
        return []

def main():
    if not os.path.exists(JSON_FILE):
        print(f"Erreur: Le fichier {JSON_FILE} n'existe pas.")
        return

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        products_data = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    create_db_and_table(conn)
    cursor = conn.cursor()
    
    print(f"Début de la génération des embeddings pour {len(products_data)} produits...")

    for i, product in enumerate(products_data):
        # Assurez-vous que ces champs correspondent à ceux de votre products.json
        sku = product.get("sku", f"SKU-{i+1}")
        title = product.get("title", "Titre Inconnu")
        price = product.get("price", 0.0)
        short_desc = product.get("short_desc", "Description courte par défaut.")
        long_desc = product.get("long_desc", "Description longue par défaut.")
        
        # Texte combiné pour l'embedding
        text_to_embed = f"{title}. {short_desc}. {long_desc}"
        
        embedding = generate_embedding(text_to_embed)
        
        if embedding:
            embedding_json = json.dumps(embedding)
            cursor.execute("""
                INSERT INTO products (sku, title, price, short_desc, long_desc, embedding) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (sku, title, price, short_desc, long_desc, embedding_json))
            print(f"Produit {i+1}/{len(products_data)}: {title} traité.")
        else:
            print(f"Produit {i+1}/{len(products_data)}: {title} ignoré (Embedding échoué).")

    conn.commit()
    conn.close()
    print(f"\n✅ Base de données {DB_PATH} créée et remplie avec {cursor.rowcount} produits.")
    print("N'oubliez pas d'exécuter les commandes Rasa et Docker ci-dessous.")

if __name__ == "__main__":
    main()