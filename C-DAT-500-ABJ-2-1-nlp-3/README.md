# 🧠 Natural Language Processing (NLP)

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/NLTK-0d4111?style=for-the-badge&logo=python&logoColor=white" alt="NLTK" />
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
</p>

## 📖 Introduction
Ce dépôt contient le projet **C-DAT-500 (NLP - Traitement du Langage Naturel)**. L'objectif de ce module est d'apprendre à appliquer les algorithmes de machine learning sur des données textuelles non structurées (text mining) pour en extraire du sens, calculer des fréquences et potentiellement réaliser des classifications supervisées ou analyser la sémantique.

## 🎯 Objectifs
- Découvrir l'analyse textuelle (récupération de livres, ex: *Alice au Pays des Merveilles*).
- Réaliser le **Preprocessing de textes** (Tokenization, Regex (suppression ponctuation), Lowercasing, Stopwords removal, Lemmatization / Stemming).
- Création de représentation vectorielle des corpus avec **Bag of Words (BoW)** ou **TF-IDF**.

## 🛠️ Stack Technique
- **NLTK (Natural Language Toolkit)** : Tokenizer, Stopwords de la langue anglaise, Stemmers.
- **Scikit-learn** : Utilisation potentielle de `TfidfVectorizer` et `CountVectorizer`.
- **Python / Pandas** pour structurer les matrices creuses résultantes ou manipuler l'I/O fichiers.

## 📂 Structure du projet
- `NLP.ipynb` et `nlp-alice2.ipynb`: Notebooks explorant l'extraction de métriques sur un corpus existant, comme le livre *Alice*, ou d'autres formats textuels.
- `file_reads.py`, `filename.py`, `python.py` : Scripts utilitaires d'accès I/O bas niveau pour l’ouverture et le formatage de fichiers bruts volumineux.
- *(Dossiers `env` / `venv`)* : Environnement virtuel isolé contenant toutes les dépendances pip spécifiques au Machine Learning NLP.

## ⚙️ Exécution
Activation de l'environnement virtuel (Si présent) puis exécution du Notebook ou du script souhaité :

**Sous MacOS/Linux**
```bash
source env/bin/activate
jupyter notebook nlp-alice2.ipynb
```

**Sous Windows**
```bash
.\env\Scripts\activate
jupyter notebook nlp-alice2.ipynb
