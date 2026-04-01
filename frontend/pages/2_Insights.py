import streamlit as st
import shap
import joblib
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

# --------------------------------
# FIX PATH (VERY IMPORTANT)
# --------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ROOT_DIR)

from src.predict import preprocess_input

# --------------------------------
# LOAD MODEL + FEATURES
# --------------------------------
model = joblib.load(os.path.join(ROOT_DIR, "models", "visa_model.pkl"))
features = joblib.load(os.path.join(ROOT_DIR, "models", "model_features.pkl"))

# --------------------------------
# UI
# --------------------------------
st.set_page_config(page_title="Insights", layout="wide")

st.title("📊 Model Explainability (SHAP)")
st.markdown("Understand why the model predicted this processing time")

# --------------------------------
# USER INPUT
# --------------------------------
visa_type = st.selectbox("Visa Type", ["H1B", "L1", "F1", "B1"])
visa_status = st.selectbox("Visa Status", ["Certified", "Denied"])
city = st.text_input("Work City", "New York")
date = st.date_input("Case Received Date")

# --------------------------------
# INPUT DATA
# --------------------------------
input_data = {
    "visa_type": visa_type,
    "visa_status": visa_status,
    "city": city,
    "case_received_date": str(date)
}

# --------------------------------
# PREPROCESS
# --------------------------------
df = preprocess_input(input_data, features)

# --------------------------------
# SHAP EXPLAINER
# --------------------------------
explainer = shap.Explainer(model)
shap_values = explainer(df)

# --------------------------------
# WATERFALL PLOT (FIXED VERSION)
# --------------------------------
st.subheader("🔍 Feature Impact on Prediction")

plt.figure()
shap.plots.waterfall(shap_values[0], show=False)

st.pyplot(plt.gcf())
plt.clf()