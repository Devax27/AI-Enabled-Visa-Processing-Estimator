import streamlit as st
import sys
import os

# 🔥 FIX: go to ROOT folder (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from src.predict import predict_processing_time

st.title("📋 Visa Prediction")

visa_type = st.selectbox("Visa Type", ["H1B", "L1", "B1", "F1"])
visa_status = st.selectbox("Visa Status", ["certified", "denied", "withdrawn"])
city = st.text_input("Working City", "New York")
date = st.date_input("Case Received Date")

st.divider()

if st.button("🚀 Predict"):

    payload = {
        "visa_type": visa_type,
        "visa_status": visa_status,
        "city": city,
        "case_received_date": str(date)
    }

    result = predict_processing_time(payload)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Prediction Complete ✅")

        st.metric("⏳ Processing Days", result["estimated_processing_days"])
        st.info(f"Confidence Range: {result['confidence_range']}")

        # 🔥 SAVE FOR PDF
        st.session_state["last_result"] = {
            "visa_type": visa_type,
            "visa_status": visa_status,
            "city": city,
            "days": result["estimated_processing_days"],
            "range": result["confidence_range"]
        }