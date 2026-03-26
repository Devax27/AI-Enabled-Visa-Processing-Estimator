import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict_processing_time

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="Visa AI", page_icon="🌍", layout="centered")

# -----------------------
# CUSTOM CSS (🔥 PREMIUM LOOK)
# -----------------------
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.main {
    background: linear-gradient(135deg, #0e1117, #1a1f2b);
}

h1 {
    text-align: center;
    font-size: 2.5rem;
    color: #00E6A8;
}

.subtitle {
    text-align: center;
    color: #A0AEC0;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: #161B22;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0, 255, 170, 0.1);
}

/* Button */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    background: linear-gradient(90deg, #00E6A8, #00C9FF);
    color: black;
    font-weight: bold;
    border: none;
}

/* Inputs */
.stTextInput input, .stSelectbox div {
    border-radius: 10px !important;
}

/* Metric card */
.metric-card {
    background: #161B22;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(0, 255, 170, 0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown("<h1>🌍 Visa AI Estimator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Smart prediction powered by Machine Learning 🚀</p>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------
# INPUT CARD
# -----------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📋 Enter Details")

    col1, col2 = st.columns(2)

    with col1:
        visa_type = st.selectbox("Visa Type", ["H1B", "L1", "B1", "F1"])
        city = st.text_input("Working City", "New York")

    with col2:
        visa_status = st.selectbox("Visa Status", ["certified", "denied", "withdrawn"])
        case_received_date = st.date_input("Case Received Date")

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------
# BUTTON
# -----------------------
st.markdown("###")

if st.button("🚀 Predict Processing Time"):

    payload = {
        "visa_type": visa_type,
        "visa_status": visa_status,
        "city": city,
        "case_received_date": str(case_received_date)
    }

    result = predict_processing_time(payload)

    st.markdown("---")

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Prediction Complete ✅")

        st.markdown("## 📊 Prediction Result")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("⏳ Processing Days", result["estimated_processing_days"])
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("📈 Confidence Range", result["confidence_range"])
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 💡 Insights")
        st.info("Prediction is based on historical visa data using ML models like XGBoost & Random Forest.")
