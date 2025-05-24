import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

class WineQualityModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)
        self.scaler = StandardScaler()

    def preprocess(self, data: np.ndarray) -> np.ndarray:
        # Cette méthode standardise les données d'entrée
        return self.scaler.transform(data)

    def predict(self, features: np.ndarray) -> np.ndarray:
        # Appliquer la standardisation sur les nouvelles données
        preprocessed_features = self.preprocess(features)
        # Effectuer la prédiction en utilisant le modèle chargé
        return self.model.predict(preprocessed_features)

# Instancier le modèle global pour éviter de le recharger à chaque requête
wine_quality_model = WineQualityModel("../app/model.pkl")
