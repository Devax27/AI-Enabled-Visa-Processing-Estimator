🚀 AI-Enabled Visa Processing Time Estimator

The AI-Enabled Visa Processing Time Estimator is a machine learning project designed to analyze historical visa application data and estimate the expected processing time for new visa applications.

This project simulates how real immigration analytics systems analyze historical workload, regional patterns, and seasonal trends to provide estimated visa processing timelines.

The system follows a complete industry-style ML pipeline, including:
Data preprocessing
Feature engineering
Model training
Hyperparameter tuning
Explainable AI
Prediction engine

🎯 Project Objective
Visa processing systems often face several challenges:
Long and unpredictable delays
Regional workload differences
Seasonal backlog surges
Lack of transparency in processing timelines

This project aims to:
Analyze visa processing trends
Engineer predictive features from historical records
Train machine learning models to estimate processing time
Provide a realistic prediction range instead of a single value
Build a production-ready ML pipeline

🧩 System Architecture
                          ┌──────────────────────────┐
                          │   Historical Visa Data   │
                          │      VisaFile.csv        │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │     Data Preprocessing   │
                          │                          │
                          │ • Column normalization   │
                          │ • Missing value handling │
                          │ • Date conversion        │
                          │ • Outlier capping (IQR)  │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │     Feature Engineering  │
                          │                          │
                          │ • Time features          │
                          │ • Regional averages      │
                          │ • Visa status signals    │
                          │ • Monthly backlog proxy  │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │ Exploratory Data Analysis│
                          │                          │
                          │ • Distribution plots     │
                          │ • Correlation heatmaps   │
                          │ • Seasonal trends        │
                          │ • Interactive charts     │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │     Model Training       │
                          │                          │
                          │ • Linear Regression      │
                          │ • Random Forest          │
                          │ • XGBoost                │
                          │ • CatBoost               │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │ Hyperparameter Tuning    │
                          │                          │
                          │ RandomizedSearchCV       │
                          │ Optimal model selection  │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │ Explainable AI Layer     │
                          │                          │
                          │ SHAP Feature Importance  │
                          │ Model Interpretation     │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │   Prediction Engine      │
                          │                          │
                          │ Estimated Processing     │
                          │ Time + Confidence Range  │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │  Web Application (Next)  │
                          │                          │
                          │ Streamlit Dashboard      │
                          │ User Input → Prediction  │
                          └──────────────────────────┘

✅ Milestone 1 – Data Collection & Preprocessing

This phase focuses on preparing a clean and reliable dataset for analysis and modeling.
Data Cleaning
Standardized column names
Handled missing values
Cleaned categorical inconsistencies
Converted date columns properly
Processing Time Calculation
A new target variable was created:
processing_time_days = decision_date − case_received_date

Additional preprocessing steps:

Removed invalid date entries
Removed negative processing durations
Outlier Handling
Applied group-wise IQR capping to reduce the effect of extreme processing times.
This is an industry-standard technique for handling outliers in operational datasets.

Visualizations Generated

The EDA pipeline automatically produces:
Processing time distribution
Correlation heatmap
Monthly trend analysis
Season vs processing comparison
Interactive Plotly histogram

All plots are automatically saved in the outputs/ directory.

✅ Milestone 2 – Industry-Level Feature Engineering

This stage transforms raw visa records into predictive signals.
Time-Based Features
Derived from application date:

year
month
quarter
season (Peak vs Off-Peak)


These simulate seasonal visa application trends.
Historical Aggregated Signals

These features capture historical processing patterns:

country_avg  → average processing time by city
visa_avg     → historical visa status average
state_avg    → regional processing average

Backlog Proxy Feature
monthly_volume


This approximates the number of visa applications submitted per month and simulates real-world backlog pressure.

✅ Milestone 3 – Predictive Modeling

This phase introduces machine learning models to estimate visa processing time.
Models Implemented
Multiple regression models were trained and compared:
Linear Regression
Random Forest
XGBoost
CatBoost

Evaluation metrics used:
MAE  – Mean Absolute Error
RMSE – Root Mean Squared Error
R²   – Coefficient of Determination

Hyperparameter Tuning
The best performing model (XGBoost) was optimized using RandomizedSearchCV.
Example tuned parameters:
n_estimators
max_depth
learning_rate
subsample
colsample_bytree


This improved the performance of the base model.
Feature Importance
The trained model identifies the most influential factors affecting visa processing time.

Example important features:

visa_class
job category (SOC title)
visa status
application month
processing year
Explainable AI (SHAP)
Model predictions were interpreted using SHAP.

SHAP helps explain:

Which features increase processing time
Which features decrease processing time

Generated outputs:

outputs/shap_summary.png
outputs/shap_feature_importance.png

Prediction Engine

A prediction module was implemented to estimate visa processing time for new cases.

Example output:

Estimated Processing Time: 125 days
Confidence Range: 100 – 150 days

The prediction range accounts for model uncertainty.

📂 Project Structure
AI-Enabled-Visa-Processing-Estimator/
│
├── src/
│   ├── eda.py
│   ├── train_model.py
│   └── predict.py
│
├── data/
│   └── VisaFile.csv
│
├── models/
│   ├── visa_model.pkl
│   ├── model_rmse.pkl
│   └── model_features.pkl
│
├── outputs/
│   ├── correlation_heatmap.png
│   ├── monthly_trend.png
│   ├── processing_time_distribution.png
│   ├── shap_summary.png
│   └── shap_feature_importance.png
│
├── requirements.txt
└── README.md

▶ How to Run the Project
Install dependencies:
pip install -r requirements.txt


Run EDA analysis:
python src/eda.py

Train the model:
python src/train_model.py

Run prediction:

python src/predict.py

⚠️ Dataset Limitation

The dataset does not include official processing center identifiers.

Regional variation was approximated using:

work_city
work_state


These act as proxies for regional workload differences.

🏆 Project Status
Milestone	Status
Milestone 1 – Data Collection	✅ Completed
Milestone 2 – Feature Engineering	✅ Completed
Milestone 3 – Predictive Modeling	✅ Completed
Milestone 4 – Web Application	⏳ Upcoming
