import numpy as np
import pandas as pd

np.random.seed(42)

n_samples = 500

sleep_hours = np.round(
    np.random.uniform(4, 9, n_samples), 1
)

study_hours = np.round(
    np.random.uniform(0.5, 6, n_samples), 1
)

break_minutes = np.random.randint(
    5, 61, n_samples
)

phone_hours = np.round(
    np.random.uniform(0.5, 6, n_samples), 1
)

stress_level = np.random.randint(
    1, 11, n_samples
)

caffeine = np.random.randint(
    0, 4, n_samples
)

previous_productivity = np.random.randint(
    30, 101, n_samples
)

score = (
    sleep_hours * 8
    + study_hours * 10
    + break_minutes * 0.15
    + previous_productivity * 0.35
    - phone_hours * 8
    - stress_level * 4
    + caffeine * 2
)

productivity = pd.cut(
    score,
    bins=[-np.inf, 80, 120, np.inf],
    labels=["Low", "Medium", "High"]
)

df = pd.DataFrame({
    "sleep_hours": sleep_hours,
    "study_hours": study_hours,
    "break_minutes": break_minutes,
    "phone_hours": phone_hours,
    "stress_level": stress_level,
    "caffeine": caffeine,
    "previous_productivity": previous_productivity,
    "productivity": productivity
})

df.to_csv(
    "data/study_sessions.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Number of records: {len(df)}")
print("\nFirst 5 records:")
print(df.head())

print("\nClass distribution:")
print(df["productivity"].value_counts())