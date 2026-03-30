import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict_processing_time

st.title("🚀 Visa Prediction")

visa_type = st.selectbox("Visa Type", ["H1B", "L1", "B1", "F1"])
visa_status = st.selectbox("Visa Status", ["certified", "denied", "withdrawn"])
city = st.text_input("Working City", "New York")
date = st.date_input("Case Received Date")

if st.button("Predict"):

    payload = {
        "visa_type": visa_type,
        "visa_status": visa_status,
        "city": city,
        "case_received_date": str(date)
    }

    result = predict_processing_time(payload)
    st.session_state["last_result"] = {
    "visa_type": visa_type,
    "visa_status": visa_status,
    "city": city,
    "days": result["estimated_processing_days"],
    "range": result["confidence_range"]
    }

    if "error" in result:
        st.error(result["error"])
    else:
        st.metric("Processing Days", result["estimated_processing_days"])
        st.info(result["confidence_range"])