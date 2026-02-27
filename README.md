🚀 AI-Enabled Visa Processing Estimator
(Milestone 1 & 2 Completed)

The AI-Enabled Visa Processing Estimator is a Python-based data science project designed to analyze historical visa application data and estimate visa processing times using structured preprocessing and feature engineering.

This project focuses on building a clean, industry-style data pipeline before moving into full machine learning modeling.

🎯 Project Objective

Visa processing systems often face:
Long and unpredictable delays
Regional workload differences
Seasonal backlogs
Lack of transparency in timelines
This project aims to:
Analyze visa processing trends
Engineer meaningful predictive features
Prepare a production-ready dataset for ML modeling

✅ Milestone 1 – 

In this phase, the focus was on understanding the dataset and cleaning inconsistencies.

✔ Data Cleaning

Standardized column names
Handled missing values
Cleaned categorical inconsistencies
Converted date columns properly

✔ Processing Time Calculation

Created processing_time_days
Removed invalid date entries
Removed negative processing durations

✔ Outlier Handling

Applied group-wise IQR capping per visa category
(Industry-standard outlier control)

✔ Visualizations Generated

Processing time distribution
Correlation heatmap
Monthly trend analysis
Visa category comparison
Missing value heatmap
Pairplot
Interactive Plotly histogram
All plots are automatically saved inside the outputs/ folder.

✅ Milestone 2 – Industry-Level Feature Engineering

This phase transforms raw data into modeling-ready signals.

🔹 Time-Based Features

year
month
quarter
season (Peak vs Off-Peak)

🔹 Historical Aggregated Signals

country_avg (city-level average processing time)
visa_avg (visa-status historical average)
state_avg (regional processing average)

🔹 Backlog Proxy Feature

monthly_volume
Approximates case load per month
Simulates real-world backlog pressure

These features mirror how real immigration dashboards analyze workload and trends.

🏗️ Project Structure
AI-Enabled-Visa-Processing-Estimator/
│
├── src/
│   └── eda.py
│
├── data/
│   └── VisaFile.csv
│
├── outputs/
│   ├── correlation_heatmap.png
│   ├── monthly_trend.png
│   ├── processing_time_distribution.png
│   ├── season_vs_processing.png
│   └── interactive_processing_time.html
│
├── requirements.txt
└── README.md

The project uses a modular structure with main() execution and path-safe file handling.

📊 Generate EDA Visualizations

Run:

python src/eda.py
All plots will be automatically generated and saved in the outputs/ directory.

🧠 Why This Approach?

Instead of jumping directly to ML models, this project focuses on:
Clean data pipelines
Strong feature engineering
Realistic backlog modeling
Reproducible structure
This ensures that when modeling begins (Milestone 3), the data foundation is strong.

⚠️ Note

The dataset does not include official processing center identifiers.
Geographic variation was analyzed using:

work_city
work_state

These serve as regional workload approximations.

🏆 Current Status

Milestone 1: ✅ Completed
Milestone 2: ✅ Completed (Industry-level feature engineering)
Milestone 3: ⏳ Upcoming
