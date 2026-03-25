import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict_processing_time

st.set_page_config(page_title="Visa AI", layout="centered")

st.title("🌍 Visa Processing Time Estimator")

visa_type = st.selectbox("Visa Type", ["H1B", "L1", "B1", "F1"])

visa_status = st.selectbox("Visa Status", ["certified", "denied", "withdrawn"])

city = st.text_input("Working City", "New York")

case_received_date = st.date_input("Case Received Date")

if st.button("🚀 Predict"):

    payload = {
        "visa_type": visa_type,
        "visa_status": visa_status,
        "city": city,
        "case_received_date": str(case_received_date)
    }

    result = predict_processing_time(payload)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Prediction Complete ✅")
        st.metric("Processing Days", result["estimated_processing_days"])
        st.info(result["confidence_range"])