
# 📊 Telecom Customer Churn Analysis & Prediction

🔗 Live App: (https://customerchurnprediction-ttumsm6b66ger3xsdcjcvf.streamlit.app/) 

## 🔹 Project Overview

This project presents an **end-to-end churn analytics and prediction pipeline** for a telecom business, combining **data cleaning, feature engineering, SQL analysis, Power BI visualization, machine learning modeling, and deployment**.

The objective is not only to predict churn, but to **understand churn drivers and support data-driven retention decisions**.

---

## 🔹 Key Business Questions Addressed

* Which customers are most likely to churn?
* What contract and billing factors drive churn?
* Where is the highest revenue risk concentrated?
* Which customers should be prioritized for retention?

---

## 🔹 Feature Engineering Highlights

Raw telecom data was enriched with business-driven features:

* **Customer Lifetime Value (CLV)**
  Estimated using tenure and monthly charges to represent customer importance.

* **Contract Risk**
  Contract types mapped into risk levels (High / Medium / Low) based on commitment length.

* **Price Sensitivity Flag**
  Identifies customers more likely to churn due to pricing behavior.

* **Tenure Buckets**
  Groups customers into lifecycle stages for cohort analysis.

⚠️ *Revenue-at-risk features were used only for analysis and post-prediction prioritization, and explicitly excluded from model training to avoid data leakage.*

---

## 🔹 Exploratory & SQL Analysis

* Cohort-based churn analysis
* Contract and payment method risk analysis
* Revenue-at-risk segmentation
* Business-focused SQL queries using MySQL and SQLAlchemy

Insights were further visualized using an **interactive Power BI dashboard**.

---

## 🔹 Machine Learning Approach

* **Problem Type:** Binary classification (Churn / No Churn)
* **Target Variable:** `churn_flag`
* **Baseline Model:** Interpretable classification model
* **Evaluation Focus:**

  * Recall for churned customers
  * ROC-AUC (preferred over accuracy due to class imbalance)

Special care was taken to **prevent feature leakage** and ensure realistic model performance.

---

## 🔹 Business Layer (Post-Prediction)

Model predictions were converted into:

* Churn probability scores
* Risk segments (Low / Medium / High)
* Revenue prioritization for retention strategies

This shifts the solution from *prediction* to *decision support*.

---

## 🔹 Deployment

The final model was deployed using **Streamlit**, allowing users to:

* Input customer attributes
* View churn probability and risk category
* Simulate retention scenarios interactively

---

## 🔹 Tools & Technologies

* **Python:** Pandas, NumPy, Scikit-learn
* **SQL:** MySQL, SQLAlchemy
* **Visualization:** Power BI
* **Deployment:** Streamlit

---

## 🔹 Why This Project Stands Out

* Business-first feature engineering
* Explicit handling of feature leakage
* Integration of analytics, ML, and deployment
* Designed for real-world decision-making, not just prediction

---

## 🔹 Final Note

This project demonstrates a **complete analytics workflow**, from raw data to deployed churn prediction, aligned with how churn problems are handled in industry.


