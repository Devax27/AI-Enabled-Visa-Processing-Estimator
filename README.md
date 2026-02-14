# 🚀 AI-Enabled Visa Processing Estimator (Milestone 1 And 2)

**AI-Enabled Visa Processing Estimator** is a Python-based machine learning project that predicts **visa application outcomes** and estimates **processing times** using historical data. It’s built to help applicants, developers, and researchers better understand trends and reduce uncertainty in visa decisions.

> 📊 With global visa systems increasingly using AI for screening and prioritization, your model can assist by offering predictions and data-driven insights rather than guesswork. :contentReference[oaicite:0]{index=0}

---

## 📌 Features

✔️ Predict the likelihood of visa approval using trained ML models  
✔ Estimate visa processing timelines based on historical trends  
✔ Analyze influential applicant and application attributes  
✔ Easy to extend with new datasets or UI improvements  
✔ Designed for research, prototyping, and visualization

---

## 🎯 Motivation

Visa applicants often face:

- Long processing delays  
- Lack of transparency on waiting time expectations  
- Uncertainty in approval chances

This project uses **machine learning** to address these challenges by learning from historical visa data and providing interpretable predictions.

---

## 🧠 How It Works

1. 📂 Load historical visa application data  
2. 🛠️ Preprocess and clean features  
3. 🤖 Train ML classification/regression models  
4. 📈 Output predicted approval probability and estimated processing time

Models can be improved as more data becomes available or with advanced techniques like ensemble learning.

---

## 🛠️ Installation

Ensure you have Python 3.8+ installed.

```bash
# Clone the repository
git clone https://github.com/Devax27/AI-Enabled-Visa-Processing-Estimator.git
cd AI-Enabled-Visa-Processing-Estimator

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux or Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
## 📊 Generate EDA Visualizations

Run:

```bash
python src/eda.py

Note: The dataset does not include processing center information. 
Therefore, geographic variation was analyzed using worksite_state 
and employer_state features.
