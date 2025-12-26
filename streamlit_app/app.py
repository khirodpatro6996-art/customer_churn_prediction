import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Config (must be FIRST)
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

# -------------------------------
# Load model & metadata
# -------------------------------
model = joblib.load("../models/churn_model_pipeline.pkl")
feature_metadata = joblib.load("../models/feature_metadata.pkl")

numerical_features = feature_metadata["numerical_features"]
categorical_features = feature_metadata["categorical_features"]

# -------------------------------
# App Title
# -------------------------------
st.title("📉 Customer Churn Prediction App")
st.write(
    "Predict customer churn risk and prioritize retention using a trained machine learning model."
)

# -------------------------------
# Input Section
# -------------------------------
st.header("🧾 Customer Information")

input_data = {}

# -------------------------------
# NUMERICAL INPUTS (CONTROLLED)
# -------------------------------

# Senior Citizen (binary)
senior_citizen_ui = st.selectbox("Senior Citizen", ["No", "Yes"])
input_data["senior_citizen"] = 1 if senior_citizen_ui == "Yes" else 0

# Tenure
tenure = st.slider("Tenure (months)", 0, 72, 12)
input_data["tenure"] = tenure

# Monthly Charges
monthly_charges = st.slider("Monthly Charges (₹)", 18, 150, 70)
input_data["monthly_charges"] = monthly_charges

# Auto-calculated Total Charges
total_charges = tenure * monthly_charges
input_data["total_charges"] = total_charges
st.caption(f"Calculated Total Charges: ₹ {total_charges:,.2f}")

# -------------------------------
# CATEGORICAL INPUTS (EXPLICIT)
# -------------------------------

input_data["gender"] = st.selectbox("Gender", ["Male", "Female"])

input_data["payment_method"] = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)",
    ],
)

input_data["contract"] = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"],
)

input_data["internet_service"] = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"],
)

input_data["tenure_bucket"] = st.selectbox(
    "Tenure Bucket",
    ["0-6 months", "6-12 months", "12-24 months", "24+ months"],
)

input_data["contract_risk"] = st.selectbox(
    "Contract Risk",
    ["Low", "Medium", "High"],
)

# -------------------------------
# 🔥 CRITICAL FIX: TYPE-SAFE FEATURE COMPLETION
# -------------------------------

# Numerical → 0
for col in numerical_features:
    if col not in input_data:
        input_data[col] = 0

# Categorical → valid string (NOT 0)
for col in categorical_features:
    if col not in input_data:
        input_data[col] = "No"

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Predict Churn Risk"):

    input_df = pd.DataFrame([input_data])

    churn_probability = model.predict_proba(input_df)[0][1]

    # Risk Segmentation
    if churn_probability < 0.4:
        risk_segment = "Low Risk"
    elif churn_probability < 0.7:
        risk_segment = "Medium Risk"
    else:
        risk_segment = "High Risk"

    predicted_revenue_at_risk = churn_probability * monthly_charges

    # -------------------------------
    # Output
    # -------------------------------
    st.subheader("📊 Prediction Results")

    st.metric("Churn Probability", f"{churn_probability:.2%}")
    st.metric("Risk Segment", risk_segment)
    st.metric(
        "Estimated Monthly Revenue at Risk",
        f"₹ {predicted_revenue_at_risk:,.2f}",
    )

    # -------------------------------
    # Explainability
    # -------------------------------
    st.subheader("🧠 Why this customer may churn")

    reasons = []

    if input_data["contract"] == "Month-to-month":
        reasons.append("Month-to-month contracts have higher churn rates")

    if tenure < 6:
        reasons.append("Short customer tenure")

    if input_data["internet_service"] == "Fiber optic":
        reasons.append("Fiber optic users historically show higher churn")

    if input_data["contract_risk"] == "High":
        reasons.append("High contract risk classification")

    if reasons:
        for r in reasons:
            st.write("•", r)
    else:
        st.write("• No strong churn risk indicators detected")

    # -------------------------------
    # Priority Message
    # -------------------------------
    if risk_segment == "High Risk":
        st.error(
            "⚠️ High priority customer – immediate retention action recommended."
        )
    elif risk_segment == "Medium Risk":
        st.warning(
            "⚠️ Medium risk – monitor and consider retention offers."
        )
    else:
        st.success(
            "✅ Low churn risk – no immediate action needed."
        )
