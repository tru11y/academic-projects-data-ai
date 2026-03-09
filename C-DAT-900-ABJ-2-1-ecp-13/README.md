# 🏆 Projet de Synthèse (ECP): Full-Stack Data App

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
</p>

## 📖 Introduction
Ce dépôt représente l'aboutissement du cycle formateur à travers le module **C-DAT-900 (Projet d'épreuve finale - ECP)**. Il s'agit d'une application complète et full-stack articulée autour de la donnée. Conçu de bout-en-bout, ce socle prend la forme d'une **Application Web Python**, agissant comme tableau de bord / interface métier branchée sur une infrastructure de base de données.

## 🎯 Fonctionnalités Clés
- **Base de Données Relationnelle** : Script d'initialisation et requêtage (`setup_db.py`, `actions.py`).
- **Data Engineering / Indexing** : Processus backend alimentant la base logicielle, comme l'indexation de produits (`index_products.py`).
- **Serveur Web Python** : Service web (`app.py`, probablement sous Flask ou librairie web allégée) mettant à disposition de l'utilisateur l'interface métier et les API REST requises.
- **Opérations CRUD (Create, Read, Update, Delete)** complètes et interactives.

## 📂 Architecture et Structure
- `app.py` : Point d'entrée de l'application web. C'est lui qui héberge et route les requêtes (Routing).
- `setup_db.py` : Script d'intégration technique et d'initialisation des schémas SQL (Migration initiale).
- `actions.py` : Entité regroupant la Business Logic (Logique Métier) ainsi que l'interface à la BDD (DAO).
- `index_products.py` : Module de peuplement (Data ingestion / Seeding) simulant des processus Data de la vie réelle.

## ⚙️ Installation et Exécution

1. **Configurer l'environnement**
Installez les pré-requis depuis un environnement virtuel Python :
```bash
pip install flask # et autres dépendances éventuelles
```

2. **Initialisation de la base de données**
Avant tout démarrage du serveur, exécutez la mise en place du Data Warehouse / de la base :
```bash
python setup_db.py
python index_products.py
```

3. **Démarrer le serveur applicatif**
Lancez votre serveur de développement local :
```bash
python app.py
```

Rendez-vous sur `http://localhost:5000` (ou port spécifié par l'application) dans votre navigateur.

---
*Ce README a été généré dans le cadre de l'audit de documentation Data/AI (Solqueflo Balley).*