# Dockerfile
FROM python:3.9-slim

# Installer les dépendances Rasa dans ce conteneur
RUN pip install rasa==3.7.0 # Assurez-vous que la version correspond à celle de votre code

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers et modèles
COPY . /app

# Définir l'ENTRYPOINT pour faciliter la commande dans docker-compose
ENTRYPOINT ["rasa"]
CMD ["run"]