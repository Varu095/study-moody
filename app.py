import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("src/study_mood_model.pkl")

st.title("📚 StudyMood AI")
st.write("Predict your study session productivity level.")
st.caption(
    "Note: This model was trained on a synthetic study-session dataset "
    "created for educational purposes."
)
st.success("Model loaded successfully!")
st.subheader("Enter your study session details")

sleep_hours = st.slider(
    "Sleep Hours",
    min_value=4.0,
    max_value=9.0,
    value=7.0,
    step=0.1
)

study_hours = st.slider(
    "Study Hours",
    min_value=0.5,
    max_value=6.0,
    value=2.0,
    step=0.1
)

break_minutes = st.slider(
    "Break Minutes",
    min_value=5,
    max_value=60,
    value=20
)

phone_hours = st.slider(
    "Phone Usage (Hours)",
    min_value=0.5,
    max_value=6.0,
    value=2.0,
    step=0.1
)

stress_level = st.slider(
    "Stress Level",
    min_value=1,
    max_value=10,
    value=5
)

caffeine = st.slider(
    "Caffeine Servings",
    min_value=0,
    max_value=3,
    value=1
)

previous_productivity = st.slider(
    "Previous Productivity",
    min_value=30,
    max_value=100,
    value=70
)
if st.button("Predict Productivity"):
    input_data = pd.DataFrame([{
        "sleep_hours": sleep_hours,
        "study_hours": study_hours,
        "break_minutes": break_minutes,
        "phone_hours": phone_hours,
        "stress_level": stress_level,
        "caffeine": caffeine,
        "previous_productivity": previous_productivity
    }])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities) * 100

    st.subheader("Prediction")

    if prediction == "High":
        st.success("Your predicted productivity level is HIGH 📈")
    elif prediction == "Medium":
        st.warning("Your predicted productivity level is MEDIUM 🙂")
    else:
        st.error("Your predicted productivity level is LOW 📉")
    st.info(f"Model confidence: {confidence:.1f}%")