# ⚙️ End-to-End Machine Learning Pipeline

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
</p>

## 📖 Introduction
Bienvenue dans le module **C-DAT-300 (End-to-End Machine Learning)**. Ce projet simule une approche de **Machine Learning de A à Z (Lifecycle)**, allant de l'extraction des données brutes jusqu'au chargement final pour l'entraînement d'un modèle algorithmique. L'approche ETL (Extract, Transform, Load) y est traitée rigoureusement.

## 🎯 Objectifs
- **Extraction** : Obtenir et structurer les sources de données initiales.
- **Transformation (Preprocessing)** : Gérer les valeurs manquantes, encoder les variables catégorielles, et normaliser ou standardiser les features quantitatives.
- **Chargement & Entraînement** : Sauvegarder les jeux de données propres pour la création d'un modèle de prédiction prêt à être évalué.

## 🛠️ Stack Technique
- **Python** orienté Data Science.
- **Pandas** & **NumPy** pour la manipulation poussée de dataframes et d'arrays.
- **Scikit-learn** pour les objets de pipeline de preprocessing (StandardScaler, SimpleImputer, OneHotEncoder).

## 📂 Structure du projet
Ce projet est découpé par étapes du pipeline de machine learning :
- `extraction_good.ipynb` : Notebook dédié à l'ingestion brute et l'analyse initiale du besoin.
- `transform_good.ipynb` : Notebook détaillant toutes les actions de transformations (Feature Engineering, nettoyage).
- `load_good.ipynb` : Notebook finalisant le format de données pour l'ingestion par un modèle (split Train/Test, modélisation).

## ⚙️ Exécution
L'exécution suit un processus ETL séquentiel. Commencez par l'extraction, la transformation puis le chargement.
```bash
jupyter notebook extraction_good.ipynb


