from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Charger le modèle MLflow
model = joblib.load("/models/model.pkl")

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
