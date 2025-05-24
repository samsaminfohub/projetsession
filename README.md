# Projet_Streamlit_FastAPI_MLFlow_wine_quality_Prediction
Prédiction qualité vin
### Aperçu - Aspect Commercial

L'évaluation de la qualité du vin est une tâche importante pour les producteurs et les distributeurs de vin. Utiliser des modèles prédictifs pour évaluer cette qualité peut aider à automatiser et à améliorer le processus de décision, garantissant ainsi que les vins de haute qualité atteignent les consommateurs tout en réduisant les coûts de production et de distribution.

Le but de ce projet est de construire un pipeline de ML prédictif (sur le dataset `wine_quality.csv`) pour évaluer la qualité du vin, afin de rendre les processus de production et de distribution plus efficaces et ciblés.

### Aperçu - Aspect Technique

Le développement traditionnel de modèles de machine learning (ML) est chronophage, gourmand en ressources et nécessite un haut degré d'expertise technique ainsi que de nombreuses lignes de code. Dans ce guide complet, nous explorons comment configurer, entraîner et servir un système ML en utilisant les capacités puissantes de Streamlit pour le frontend, FastAPI pour le backend, MLflow pour la gestion des modèles, ainsi que Docker et Docker-Compose pour containeriser l'ensemble du projet afin de construire un modèle de prédiction de la qualité du vin.

### Objectif

Rendre les processus de production et de distribution de vin plus efficaces et ciblés en construisant un pipeline de ML prédictif pour évaluer la qualité du vin.

### Composants du Pipeline

1. Acquisition et Prétraitement des Données
2. Entraînement de modèles ML avec suivi MLflow
3. Déploiement du meilleur modèle via FastAPI
4. Interface utilisateur Streamlit pour poster des données de test au point de terminaison FastAPI
5. Containerisation avec Docker et Docker-Compose

### Dossier de Projet

# TP3 Project

## Description
Ce projet consiste à prédire la qualité du vin en utilisant différentes approches de machine learning et à déployer les modèles entraînés dans un environnement multi-conteneurs à l'aide de Docker et Docker Compose.

## Structure du Projet

```
TP3/
│
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── download_dataset.py
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       └── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│
├── notebook/
│   ├── eda.ipynb
│   ├── train_model.ipynb
│
├── mlflow/
│   ├── Dockerfile
│   ├── requirements.txt
│
├── docker-compose.yaml
├── mlruns/
├── data/
│   └── winequality-red.csv
├── Readme.txt
└── captures/
```

### Références

1. https://hub.docker.com/
2. https://github.com/
3. https://streamlit.io/
4. https://fastapi.tiangolo.com/

