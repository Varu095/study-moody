import joblib
from pathlib import Path
# Make prediction
import pandas as pd


# Find the model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "study_mood_model.pkl"

# Load the trained model
model = joblib.load(MODEL_PATH)

print("Study Mood Model Loaded Successfully!")
print()

# Take user input
sleep_hours = float(input("Enter sleep hours: "))
study_hours = float(input("Enter study hours: "))
break_minutes = float(input("Enter break minutes: "))
phone_hours = float(input("Enter phone usage hours: "))
stress_level = float(input("Enter stress level (1-10): "))
caffeine = float(input("Enter caffeine intake: "))
previous_productivity = float(input("Enter previous productivity: "))

input_data = pd.DataFrame([{
    "sleep_hours": sleep_hours,
    "study_hours": study_hours,
    "break_minutes": break_minutes,
    "phone_hours": phone_hours,
    "stress_level": stress_level,
    "caffeine": caffeine,
    "previous_productivity": previous_productivity
}])

prediction = model.predict(input_data)

print()
print("Predicted Study Mood:", prediction[0])