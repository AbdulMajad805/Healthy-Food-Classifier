import streamlit as st
import numpy as np
import pickle

# -----------------------------
# LOAD MODEL + FEATURES
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))
feature_names = pickle.load(open("features.pkl", "rb"))

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Healthy Food Predictor", layout="centered")

st.title("🍛 Healthy Indian Food Predictor")
st.markdown("### Enter nutritional values to check if food is healthy")

# -----------------------------
# SECTION 1: BASIC NUTRITION
# -----------------------------
st.subheader("🍽️ Basic Nutrition")

col1, col2 = st.columns(2)

with col1:
    calories = st.slider("Calories (kcal)", 0, 2000, 500)  # doubled
    carbs = st.slider("Carbohydrates (g)", 0, 300, 100)
    protein = st.slider("Protein (g)", 0, 100, 20)

with col2:
    fat = st.slider("Fats (g)", 0, 100, 20)
    sugar = st.slider("Free Sugar (g)", 0, 100, 20)
    fiber = st.slider("Fibre (g)", 0, 60, 10)

# -----------------------------
# SECTION 2: MICRONUTRIENTS
# -----------------------------
with st.expander("🧪 Advanced Micronutrients (Optional)"):
    sodium = st.slider("Sodium (mg)", 0, 4000, 1000)
    calcium = st.slider("Calcium (mg)", 0, 2000, 400)
    iron = st.slider("Iron (mg)", 0, 40, 10)
    vitamin_c = st.slider("Vitamin C (mg)", 0, 200, 40)
    folate = st.slider("Folate (µg)", 0, 1000, 200)

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
if calories != 0:
    protein_ratio = protein / calories
    fat_ratio = fat / calories
    carb_ratio = carbs / calories
    nutrient_density = (protein + fiber) / calories
else:
    protein_ratio = 0
    fat_ratio = 0
    carb_ratio = 0
    nutrient_density = 0

# -----------------------------
# CREATE INPUT DICTIONARY
# -----------------------------
input_dict = {
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

# -----------------------------
# ALIGN FEATURES (CRITICAL FIX)
# -----------------------------
features = np.array([[input_dict[col] for col in feature_names]])

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🔍 Predict Health Status"):

    try:
        prediction = model.predict(features)

        st.subheader("Result:")

        if prediction[0] == 1:
            st.success("✅ Healthy Food")
            st.markdown("💡 Good balance of nutrients")
        else:
            st.error("❌ Unhealthy Food")
            st.markdown("⚠️ High fat, sugar, or calories detected")

    except Exception as e:
        st.error("⚠️ Model input mismatch. Please check feature alignment.")
        st.text(str(e))

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning & Streamlit")
