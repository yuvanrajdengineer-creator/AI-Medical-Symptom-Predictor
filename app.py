import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ---- Load Model Variables (using the same ones we trained earlier) ----

symptoms = ["itching", "skin_rash", "continuous_sneezing", "fatigue", "high_fever", "headache", "nausea"]

# Use previously trained model
st.title("🩺 AI Medical Symptom Checker")

st.write("This tool predicts a possible disease based on selected symptoms. For educational use only — not medical advice.")

user_input = []

for symptom in symptoms:
    user_input.append(st.checkbox(symptom.replace("_", " ").title()))

input_array = np.array(user_input).reshape(1, -1)

if st.button("Predict Disease"):
    pred = model.predict(input_array)[0]
    disease = label_encoder.inverse_transform([pred])[0]
    st.success(f"🧠 Predicted Condition: *{disease}*"
