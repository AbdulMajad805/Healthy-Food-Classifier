import streamlit as st
import numpy as np
import pickle

# Load trained model (you must save it first)
model = pickle.load(open("model.pkl", "rb"))

st.title("🍛 Healthy Food Classification App")
st.write("Enter nutritional values to check if food is Healthy or Unhealthy")

# User Inputs
calories = st.number_input("Calories (kcal)", min_value=0.0)
protein = st.number_input("Protein (g)", min_value=0.0)
fat = st.number_input("Fats (g)", min_value=0.0)
carbs = st.number_input("Carbohydrates (g)", min_value=0.0)
sugar = st.number_input("Free Sugar (g)", min_value=0.0)
fiber = st.number_input("Fibre (g)", min_value=0.0)

# Feature Engineering (same as notebook)
protein_ratio = protein / calories if calories != 0 else 0
fat_ratio = fat / calories if calories != 0 else 0
carb_ratio = carbs / calories if calories != 0 else 0
nutrient_density = (protein + fiber) / calories if calories != 0 else 0

features = np.array([[calories, protein, fat, carbs, sugar, fiber,
                      protein_ratio, fat_ratio, carb_ratio, nutrient_density]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Healthy Food")
    else:
        st.error("❌ Unhealthy Food")