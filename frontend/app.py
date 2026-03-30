import streamlit as st

st.set_page_config(page_title="Visa AI", page_icon="🌍")

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

h1 {
    text-align: center;
    color: #00ffd5;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Visa AI System")

st.markdown("### 🚀 Smart Visa Processing Prediction Platform")

st.markdown("""
<div class="card">
<h3>✨ What this system does</h3>
<ul>
<li>Predict visa processing time</li>
<li>Show intelligent insights</li>
<li>Generate downloadable reports</li>
<li>Provide real-time analytics</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.success("Use sidebar to explore features 🚀")