import streamlit as st
import requests

st.title("Wine Quality Prediction")

fixed_acidity = st.slider("Fixed Acidity", 4.0, 15.0)
volatile_acidity = st.slider("Volatile Acidity", 0.1, 1.5)
citric_acid = st.slider("Citric Acid", 0.0, 1.0)
residual_sugar = st.slider("Residual Sugar", 0.9, 15.0)
chlorides = st.slider("Chlorides", 0.01, 0.2)
free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1, 72)
total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 6, 289)
density = st.slider("Density", 0.990, 1.005)
pH = st.slider("pH", 2.8, 4.0)
sulphates = st.slider("Sulphates", 0.3, 2.0)
alcohol = st.slider("Alcohol", 8.0, 15.0)

if st.button("Predict"):
    response = requests.post("http://api:8000/predict", json={
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol
    })
    prediction = response.json()["prediction"]
    st.write(f"The predicted wine quality is: {prediction}")
