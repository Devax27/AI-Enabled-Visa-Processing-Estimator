import streamlit as st
import plotly.express as px
from datetime import date
from src.predict import predict_processing_time

# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="Visa AI Estimator",
    layout="wide"
)

# --------------------------------
# Custom Styling (Beautiful UI)
# --------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
h1, h2, h3 {
    color: #00d4ff;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# Title
# --------------------------------
st.title("🌍 AI Visa Processing Time Estimator")
st.markdown("### Predict visa processing time using Machine Learning + AI")

# --------------------------------
# Sidebar Inputs
# --------------------------------
st.sidebar.header("📋 Enter Visa Details")

visa_type = st.sidebar.selectbox(
    "Visa Type",
    ["H1B", "L1", "F1", "B1"]
)

visa_status = st.sidebar.selectbox(
    "Visa Status",
    ["Certified", "Denied"]
)

city = st.sidebar.text_input(
    "Work City",
    "New York"
)

received_date = st.sidebar.date_input(
    "Case Received Date",
    date.today()
)

# --------------------------------
# Prediction Button
# --------------------------------
if st.sidebar.button("🚀 Predict Processing Time"):

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
            st.metric(
                "Estimated Processing Days",
                result["estimated_processing_days"]
            )

        with col2:
            st.metric(
                "Confidence Range",
                result["confidence_range"]
            )

        # --------------------------------
        # Visualization
        # --------------------------------
        st.subheader("📊 Processing Time Visualization")

        fig = px.bar(
            x=["Processing Time"],
            y=[result["estimated_processing_days"]],
            title="Estimated Processing Time"
        )

        st.plotly_chart(fig)

# --------------------------------
# Agentic AI Assistant (Unique Feature)
# --------------------------------
st.subheader("🤖 AI Visa Assistant")

user_query = st.text_input(
    "Ask anything about visa processing (e.g., delays, tips, approval chances)"
)

if st.button("Ask AI"):

    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = f"""
        🔍 Based on your query:

        👉 Visa Type: {visa_type}
        👉 Location: {city}

        💡 Insights:
        - Processing times depend on workload and visa category
        - Peak months (Dec–Feb) are slower
        - Ensure documentation is complete

        📌 Recommendation:
        Apply early and track your application regularly.
        """

        st.info(response)

# --------------------------------
# Footer
# --------------------------------
st.markdown("---")
st.markdown("Built with ❤️ using Machine Learning + Streamlit")