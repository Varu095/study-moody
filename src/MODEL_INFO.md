# Study Mood Prediction Model

## Model Details

* **Model:** Random Forest Classifier
* **Task:** Study Mood Classification
* **Model File:** `study_mood_model.pkl`
* **Training Notebook:** `../notebooks/eda.ipynb`

## Features Used

The model uses these 7 input features:

1. Sleep Hours
2. Study Hours
3. Break Minutes
4. Phone Usage Hours
5. Stress Level
6. Caffeine Intake
7. Previous Productivity

## Prediction

The model predicts the student's study mood based on the above factors.

Possible output:

* **Low**
* **Medium**
* **High**

## How to Run

From the project root:

```bash
python src/predict.py
```

The program will ask for the 7 inputs and display the predicted study mood.

## Model File

The trained model is stored as:

```text
src/study_mood_model.pkl
```

The `.pkl` file is a binary model file, so GitHub cannot display its internal contents as normal text. This file is loaded by `predict.py` using `joblib`.
