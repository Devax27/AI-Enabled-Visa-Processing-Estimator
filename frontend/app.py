import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict_processing_time

st.set_page_config(page_title="Visa AI", layout="centered")

st.title("🌍 Visa Processing Time Estimator")
st.markdown("Enter details to predict processing time")

year = st.number_input("Year", value=2023)
month = st.selectbox("Month", list(range(1, 13)))
quarter = st.selectbox("Quarter", [1, 2, 3, 4])
visa_type = st.selectbox("Visa Type", ["H1B", "L1", "B1", "F1"])
visa_status = st.selectbox("Visa Status", ["Certified", "Denied", "Withdrawn"])
wage = st.number_input("Wage Submitted", value=50000)
unit = st.selectbox("Wage Unit", ["Year", "Month", "Week", "Hour"])

if st.button("🚀 Predict"):

    payload = {
        "year": int(year),
        "month": int(month),
        "quarter": int(quarter),
        "visa_type": visa_type,
        "visa_status": visa_status,
        "wage": wage,
        "unit": unit
    }

    try:
        result = predict_processing_time(payload)

        st.success("Prediction Complete ✅")
        st.subheader("📊 Prediction Result")

        st.write("Predicted Visa Outcome:", result.get("predicted_status", "N/A"))

        st.metric("Processing Days", result["estimated_processing_days"])
        st.info(f"Confidence Range: {result['confidence_range']}")

    except Exception as e:
        st.error(f"Error: {e}")