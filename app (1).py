
import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="California AQI Risk Predictor", page_icon="🌫️", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("random_forest_model.sav")

@st.cache_resource
def load_scaler():
    return joblib.load("scaler.sav")

model = load_model()
scaler = load_scaler()

st.title("🌫️ California AQI Risk Predictor")
st.caption("Random Forest · County-Level · Binary Classification")

ozone = st.number_input("Ozone (ppm)", min_value=0.000, max_value=0.200, value=0.040, step=0.001, format="%.3f")
population_raw = st.number_input("County Population", min_value=1000, max_value=10000000, value=500000, step=10000)
tmax = st.number_input("Max Temp (°F)", min_value=20, max_value=130, value=75)
tmin = st.number_input("Min Temp (°F)", min_value=0, max_value=110, value=55)
awnd = st.number_input("Wind Speed (mph)", min_value=0.0, max_value=60.0, value=7.0, step=0.5)
prcp = st.number_input("Precipitation (in)", min_value=0.00, max_value=10.00, value=0.00, step=0.01, format="%.2f")
season_label = st.selectbox("Season", ["Winter (Dec-Feb)", "Spring (Mar-May)", "Summer (Jun-Aug)", "Fall (Sep-Nov)"])
is_weekend = st.selectbox("Day Type", ["Weekday", "Weekend"])

season_map = {"Winter (Dec-Feb)": 1, "Spring (Mar-May)": 2, "Summer (Jun-Aug)": 3, "Fall (Sep-Nov)": 4}
season = season_map[season_label]
is_weekend_val = 1 if is_weekend == "Weekend" else 0
is_rainy = 1 if prcp > 0 else 0
temp_range = tmax - tmin
season_2 = 1 if season == 2 else 0
season_3 = 1 if season == 3 else 0
season_4 = 1 if season == 4 else 0

population_scaled = scaler.transform([[population_raw]])[0][0]

features = np.array([[ozone, is_weekend_val, population_scaled, prcp, tmax, tmin, awnd, temp_range, is_rainy, season_2, season_3, season_4]])

if st.button("Run Prediction", use_container_width=True):
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0]
    if prediction == 1:
        st.error(f" UNSAFE AQI PREDICTED — Risk probability: {prob[1]*100:.1f}%")
    else:
        st.success(f" SAFE AQI PREDICTED — Safe probability: {prob[0]*100:.1f}%")
