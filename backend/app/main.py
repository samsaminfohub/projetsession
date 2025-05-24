from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
import pickle
import os

app = FastAPI()

# Charger le modèle MLflow
#model = joblib.load("../app/model.pkl")

class WineQuality(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

# Définir le chemin correct pour model.pkl
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

# Vérifier si le fichier existe
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Le fichier {model_path} n'existe pas")

# Charger le modèle formé
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(wine: WineQuality):
    data = np.array([[
        wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid,
        wine.residual_sugar, wine.chlorides, wine.free_sulfur_dioxide,
        wine.total_sulfur_dioxide, wine.density, wine.pH,
        wine.sulphates, wine.alcohol
    ]])
    prediction = model.predict(data)
    return {"prediction": prediction[0]}
