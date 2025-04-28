# app.py

import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("salary2025_model(1).pkl", "rb") as f:
    model = pickle.load(f)

# Define education mapping
education_mapping = {'HS': 0, 'BS': 1, 'MS': 2, 'PHD': 3}

# App Title
st.set_page_config(page_title="Salary Predictor", page_icon="💼")
st.title("💼 Data Scientist Salary Predictor")
st.subheader("Estimate your salary based on skills, experience, education, and learning platforms.")

# User Inputs
education = st.selectbox("Education Level", list(education_mapping.keys()))
years_coding = st.slider("Years of Coding Experience", 0, 40, 5)
country = st.selectbox("Country", ["United States", "United Kingdom", "Germany", "Other"])
codes_java = st.checkbox("Codes in Java")
codes_python = st.checkbox("Codes in Python")
codes_sql = st.checkbox("Codes in SQL")
codes_go = st.checkbox("Codes in Go")

# ➔ Alternative Learning Platforms
alt_learning = st.multiselect(
    "Alternative Learning Platforms Used:",
    ["Coursera", "Kaggle Learn", "Udemy"]
)

# Mapping inputs
education_num = education_mapping[education]

features = {
    "Education": education_num,
    "YearsCoding": years_coding,
    "Java": int(codes_java),
    "Python": int(codes_python),
    "SQL": int(codes_sql),
    "Go": int(codes_go),
    "Country_Germany": 0,
    "Country_United Kingdom": 0,
    "Country_United States": 0,
}

if country == "United States":
    features["Country_United States"] = 1
elif country == "United Kingdom":
    features["Country_United Kingdom"] = 1
elif country == "Germany":
    features["Country_Germany"] = 1

input_data = pd.DataFrame([features])

# ➔ Platform Bonus
platform_bonus = len(alt_learning) * 1000

# Salary Prediction Section
st.markdown("### 🧮 Salary Prediction")

if st.button("💵 Predict Salary"):
    prediction = model.predict(input_data)[0]
    prediction += platform_bonus
    st.success(f"Estimated Salary: **${prediction:,.2f}**")

# Footer
st.markdown("---")
st.markdown(
    "<small>Built with Streamlit</small>",
    unsafe_allow_html=True
)
