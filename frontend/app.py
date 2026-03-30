import streamlit as st

st.set_page_config(page_title="Visa AI", page_icon="🌍", layout="centered")

# -----------------------
# PREMIUM CSS (OFFICIAL LOOK)
# -----------------------
st.markdown("""
<style>

/* Background */
body {
    background-color: #f4f7fb;
}

/* Main container */
.main {
    background-color: #f4f7fb;
}

/* Title */
h1 {
    text-align: center;
    color: #003366;
    font-weight: bold;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #4a5568;
}

/* Card */
.card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-top: 20px;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 8px;
    background-color: #0056b3;
    color: white;
    font-weight: bold;
    border: none;
}

/* Input fields */
.stTextInput input, .stSelectbox div {
    border-radius: 8px !important;
}

/* Divider */
hr {
    border: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown("<h1>🌍 Visa Processing System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Official-style AI platform for visa processing insights</p>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------
# CONTENT CARD
# -----------------------
st.markdown("""
<div class="card">
<h3>📌 About the System</h3>
<p>
This platform uses machine learning to estimate visa processing time based on historical data.
It provides insights and predictive analytics to help applicants better understand expected timelines.
</p>

<h4>✨ Key Capabilities</h4>
<ul>
<li>✔ Visa processing time prediction</li>
<li>✔ Data-driven insights dashboard</li>
<li>✔ Report generation</li>
<li>✔ Real-time analysis</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.success("Use the sidebar to navigate through the system")