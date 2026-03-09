# 🐘 Big Data Data Pipeline

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
</p>

## 📖 Introduction
Ce dépôt couvre le module **C-DAT-700 (Big Data)**. Son but est d'étendre la science de la donnée expérimentée au gré des architectures locales aux environnements requérant un traitement distribué, scalable, ou des manipulations adaptées aux forts volumes historiques (ex: Datasets médicaux exhaustifs).

## 🎯 Objectifs
- Analyser des datasets massifs avec des contraintes temps-machine via une optimisation de code Python.
- Effectuer des analyses médicales prédictives ou exploratoires sur des Use-Cases concrets comme des registres de cellules cancéreuses.
- Expérimentation avec des concepts ou API permettant le traitement parallélisé (Spark, Dask, ou Chunking natif en Pandas).

## 📂 Structure du projet
- `Breast_Cancer.ipynb` : Notebook de Big Data Analytics sur un dataset médical (Breast Cancer) visant la classification ou la prédiction dans l'espace multidimensionnel.
- `admin's Python notebook.ipynb` : Script et notes de validation pour exécution locale massifiée.

## ⚙️ Exécution
L'exécution se fait sur environnement scientifique usuel ou JupyterHub selon la machine cloud / locale :
```bash
jupyter notebook Breast_Cancer.ipynb
