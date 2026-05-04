import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Healthy Food Predictor", layout="centered")

st.title("🍛 Healthy Indian Food Predictor")
st.markdown("### Check if a food item is healthy based on its nutrition")

# -----------------------------
# SECTION 1: BASIC NUTRITION
# -----------------------------
st.subheader("🍽️ Basic Nutrition")

col1, col2 = st.columns(2)

with col1:
    calories = st.slider("Calories (kcal)", 0, 1000, 300)
    carbs = st.slider("Carbohydrates (g)", 0, 150, 50)
    protein = st.slider("Protein (g)", 0, 50, 10)

with col2:
    fat = st.slider("Fats (g)", 0, 50, 10)
    sugar = st.slider("Free Sugar (g)", 0, 50, 10)
    fiber = st.slider("Fibre (g)", 0, 30, 5)

# -----------------------------
# SECTION 2: MICRONUTRIENTS
# -----------------------------
with st.expander("🧪 Advanced Micronutrients (Optional)"):
    sodium = st.slider("Sodium (mg)", 0, 2000, 500)
    calcium = st.slider("Calcium (mg)", 0, 1000, 200)
    iron = st.slider("Iron (mg)", 0, 20, 5)
    vitamin_c = st.slider("Vitamin C (mg)", 0, 100, 20)
    folate = st.slider("Folate (µg)", 0, 500, 100)

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
# FEATURE VECTOR (CRITICAL ORDER)
# -----------------------------
features = np.array([[
    calories,
    carbs,
    protein,
    fat,
    sugar,
    fiber,
    sodium,
    calcium,
    iron,
    vitamin_c,
    folate,
    protein_ratio,
    fat_ratio,
    carb_ratio,
    nutrient_density
]])

# -----------------------------
# PREDICTION BUTTON
# -----------------------------
if st.button("🔍 Predict Health Status"):

    prediction = model.predict(features)

    st.subheader("Result:")

    if prediction[0] == 1:
        st.success("✅ This food is HEALTHY")
        st.markdown("💡 *Good balance of nutrients and lower unhealthy components*")
    else:
        st.error("❌ This food is UNHEALTHY")
        st.markdown("⚠️ *High calories, fat, or sugar may be present*")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning & Streamlit")
