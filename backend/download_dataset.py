import os
import requests

# URL du dataset
dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
# Chemin où le dataset sera sauvegardé
dataset_path = "data/winequality-red.csv"

# Créer le répertoire 'data' s'il n'existe pas
os.makedirs(os.path.dirname(dataset_path), exist_ok=True)

# Télécharger le dataset
response = requests.get(dataset_url)
response.raise_for_status()  # Vérifie si la requête a réussi

# Sauvegarder le dataset dans le fichier spécifié
with open(dataset_path, "wb") as f:
    f.write(response.content)

print(f"Dataset téléchargé et sauvegardé à {dataset_path}")
