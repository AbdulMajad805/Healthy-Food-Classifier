import streamlit as st
import numpy as np
import pickle

# Load model and features
model = pickle.load(open("model.pkl", "rb"))
feature_names = pickle.load(open("features.pkl", "rb"))

st.title("🍛 Healthy Food Predictor")

# Inputs (same as before)
calories = st.slider("Calories", 0, 2000, 500)
carbs = st.slider("Carbs", 0, 300, 100)
protein = st.slider("Protein", 0, 100, 20)
fat = st.slider("Fat", 0, 100, 20)
sugar = st.slider("Sugar", 0, 100, 20)
fiber = st.slider("Fiber", 0, 60, 10)

sodium = st.slider("Sodium", 0, 4000, 1000)
calcium = st.slider("Calcium", 0, 2000, 400)
iron = st.slider("Iron", 0, 40, 10)
vitamin_c = st.slider("Vitamin C", 0, 200, 40)
folate = st.slider("Folate", 0, 1000, 200)

# Engineered features
protein_ratio = protein / calories if calories != 0 else 0
fat_ratio = fat / calories if calories != 0 else 0
carb_ratio = carbs / calories if calories != 0 else 0
nutrient_density = (protein + fiber) / calories if calories != 0 else 0

# ALL possible features
all_features = {
    'Calories (kcal)': calories,
    'Carbohydrates (g)': carbs,
    'Protein (g)': protein,
    'Fats (g)': fat,
    'Free Sugar (g)': sugar,
    'Fibre (g)': fiber,
    'Sodium (mg)': sodium,
    'Calcium (mg)': calcium,
    'Iron (mg)': iron,
    'Vitamin C (mg)': vitamin_c,
    'Folate (µg)': folate,
    'protein_ratio': protein_ratio,
    'fat_ratio': fat_ratio,
    'carb_ratio': carb_ratio,
    'nutrient_density': nutrient_density
}

# 🔥 KEY FIX: match EXACT features
features = np.array([[all_features.get(col, 0) for col in feature_names]])

# Predict
if st.button("Predict"):
    pred = model.predict(features)
    if pred[0] == 1:
        st.success("✅ Healthy")
    else:
        st.error("❌ Unhealthy")
