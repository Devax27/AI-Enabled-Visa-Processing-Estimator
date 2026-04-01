import streamlit as st
import plotly.express as px
from datetime import date
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..") ))

from src.predict import predict_processing_time

st.title("🔮 Visa Processing Time Prediction")

# Sidebar Inputs
visa_type = st.selectbox("Visa Type", ["H1B", "L1", "F1", "B1"])
visa_status = st.selectbox("Visa Status", ["Certified", "Denied"])
city = st.text_input("Work City", "New York")
received_date = st.date_input("Case Received Date", date.today())

if st.button("Predict"):

    input_data = {
        "visa_type": visa_type,
        "visa_status": visa_status,
        "city": city,
        "case_received_date": str(received_date)
    }

    result = predict_processing_time(input_data)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Prediction Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Estimated Days", result["estimated_processing_days"])

        with col2:
            st.metric("Confidence Range", result["confidence_range"])

        # Visualization
        fig = px.bar(
            x=["Processing Time"],
            y=[result["estimated_processing_days"]],
            title="Estimated Processing Time"
        )

        st.plotly_chart(fig)