import streamlit as st
import plotly.express as px
from datetime import date
import sys
import os

# --------------------------------
# FIX IMPORT PATH (VERY IMPORTANT)
# --------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ROOT_DIR)

from src.predict import predict_processing_time

# --------------------------------
# UI
# --------------------------------
st.set_page_config(page_title="Prediction", layout="wide")

st.title("🔮 Visa Processing Time Prediction")

# Inputs
visa_type = st.selectbox("Visa Type", ["H1B", "L1", "F1", "B1"])
visa_status = st.selectbox("Visa Status", ["Certified", "Denied"])
city = st.text_input("Work City", "New York")
received_date = st.date_input("Case Received Date", date.today())

# Prediction
if st.button("🚀 Predict"):

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
        st.success("✅ Prediction Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Estimated Days", result["estimated_processing_days"])

        with col2:
            st.metric("Confidence Range", result["confidence_range"])

        # Visualization
        st.subheader("📊 Visualization")

        fig = px.bar(
            x=["Processing Time"],
            y=[result["estimated_processing_days"]],
            title="Estimated Processing Time"
        )

        st.plotly_chart(fig)