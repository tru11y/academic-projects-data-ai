# Rasa + GPT WhatsApp Chatbot — Projet clé en main

Fichiers inclus:
- actions.py
- domain.yml
- nlu.yml
- rules.yml
- endpoints.yml
- credentials.yml (à remplir)
- products.json (extrait de ta base)
- index_products.py
- requirements.txt
- Dockerfile
- .env.example

Étapes rapides:
1. Copier `.env.example` -> `.env` et compléter les valeurs (OPENAI_API_KEY, TWILIO creds).
2. Installer dépendances: `pip install -r requirements.txt`.
3. Indexer les produits: `python3 index_products.py`.
4. Lancer Rasa (dev): `rasa run --enable-api`.
5. Lancer actions server: `rasa run actions` ou `python -m rasa_sdk` (dans un shell séparé).
6. Connecter Twilio WhatsApp sandbox -> config webhook -> tester.

Notes:
- Pour la production, remplace SQLite par Pinecone/Qdrant pour l'index vectoriel.
- Ajuste `max_tokens` / `temperature` pour contrôler coûts.