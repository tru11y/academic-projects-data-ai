import streamlit as st
import requests
import json
import time

# --- Configuration du Serveur Rasa ---
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"
SENDER_ID = "streamlit_user"

st.set_page_config(
    page_title="Démonstration Rasa Chatbot",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("🤖 Démonstration Chatbot Rasa")

# Instructions pour l'utilisateur
st.markdown("""
Bienvenue dans l'interface de démonstration !
Assurez-vous que le **Serveur Rasa Core** (port 5005) et le **Serveur d'Actions** (port 5055) sont lancés localement avant d'interagir.
""")


def send_message_to_rasa(message):
    """Envoie le message à l'API Rasa et retourne la réponse."""
    try:
        # Prépare le payload
        payload = {
            "sender": SENDER_ID,
            "message": message
        }
        # Envoie la requête POST à Rasa
        response = requests.post(RASA_SERVER_URL, json=payload, timeout=30)
        
        # Vérifie si la requête a réussi (code 200)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Erreur de l'API Rasa : Statut {response.status_code}. Vérifiez les logs des terminaux Rasa.")
            return []
            
    except requests.exceptions.ConnectionError:
        st.error("Erreur de connexion. Le Serveur Rasa (port 5005) n'est pas accessible. Veuillez le lancer.")
        return []
    except requests.exceptions.Timeout:
        st.error("Délai de réponse dépassé. Le Serveur d'Actions est peut-être lent.")
        return []
    except Exception as e:
        st.error(f"Une erreur inattendue s'est produite : {e}")
        return []


# --- Gestion de l'état de la conversation (Chat History) ---
if "messages" not in st.session_state:
    # Initialise l'historique de chat au démarrage
    st.session_state["messages"] = [
        {"role": "bot", "content": "Bonjour ! Je suis votre assistant. Que puis-je faire pour vous ?"}
    ]

# --- Affichage de l'historique des messages ---
chat_container = st.container()

with chat_container:
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- Champ de saisie pour l'utilisateur ---
if user_input := st.chat_input("Votre message..."):
    
    # 1. Ajoute le message de l'utilisateur à l'historique
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # 2. Réaffiche l'historique immédiatement (pour inclure le message utilisateur)
    with chat_container:
        with st.chat_message("user"):
            st.markdown(user_input)

    # 3. Envoie le message à Rasa et gère la réponse
    with st.spinner("Le bot réfléchit..."):
        rasa_responses = send_message_to_rasa(user_input)

    # 4. Traite et affiche les réponses du bot
    if rasa_responses:
        for response in rasa_responses:
            bot_text = response.get("text")
            
            if bot_text:
                # Ajoute la réponse du bot à l'historique et l'affiche
                st.session_state["messages"].append({"role": "bot", "content": bot_text})
                
                with chat_container:
                    with st.chat_message("bot"):
                        st.markdown(bot_text)

# Le bouton de réinitialisation est utile pour recommencer une conversation
if st.button("Démarrer une nouvelle conversation"):
    st.session_state["messages"] = [
        {"role": "bot", "content": "Bonjour ! Nouvelle conversation démarrée. Que puis-je faire pour vous ?"}
    ]
    st.rerun()