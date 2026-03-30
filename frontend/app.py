import streamlit as st

st.set_page_config(page_title="Visa AI", page_icon="🌍", layout="centered")

# -----------------------
# 🌈 PREMIUM CSS + ANIMATION
# -----------------------
st.markdown("""
<style>

/* Background Gradient */
.main {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #0ea5e9);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
}

/* Animation */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Title */
h1 {
    text-align: center;
    color: #ffffff;
    font-weight: 700;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #e2e8f0;
    font-size: 1.1rem;
}

/* Glass Card */
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
    margin-top: 20px;
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    background: linear-gradient(90deg, #22c55e, #06b6d4);
    color: white;
    font-weight: bold;
    border: none;
}

/* Inputs */
.stTextInput input, .stSelectbox div {
    border-radius: 10px !important;
}

/* Divider */
hr {
    border: 1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown("<h1>🌍 Visa AI System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Smart visa processing prediction powered by AI 🚀</p>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------
# CONTENT CARD
# -----------------------
st.markdown("""
<div class="card">
<h3>✨ What this platform does</h3>
<ul>
<li>🚀 Predict visa processing time using ML</li>
<li>📊 Show insights & trends</li>
<li>📄 Generate downloadable reports</li>
<li>⚡ Real-time prediction system</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>📌 How to use</h3>
<ol>
<li>Go to Predict page</li>
<li>Enter your details</li>
<li>Click predict</li>
<li>View insights & download report</li>
</ol>
</div>
""", unsafe_allow_html=True)

# -----------------------
# FOOTER EFFECT
# -----------------------
st.markdown("###")

st.success("✨ Navigate using sidebar to explore features")