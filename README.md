# 📚 StudyMood AI

> **Can a machine learning model guess how productive your next study session might be? 👀**

We've all had that moment:

**"Today I'm going to study seriously."**

Then comes the phone.  
Then a break.  
Then another break.  
And somehow 2 hours are gone. 😭

So I thought — why not build a small ML project around it?

**StudyMood AI** is a machine learning project that predicts the productivity level of a study session as:

- 🟢 **High**
- 🟡 **Medium**
- 🔴 **Low**

The project takes a few study-related inputs, passes them through a trained machine learning model, and gives a predicted productivity level through a simple Streamlit web app.

---

## 💡 What is StudyMood AI?

StudyMood AI was created as a hands-on machine learning project to understand the complete journey of an ML project instead of stopping at model training.

The project goes through:

```text
Create Data
    ↓
Explore Data
    ↓
Train Model
    ↓
Evaluate Model
    ↓
Make Predictions
    ↓
Build a Web App

So this project is not just about:

"I trained a Random Forest model."

It is about understanding what happens before and after model training too.

🎯 What does the model look at?

The model uses these study-session features:

Feature	Description
😴 sleep_hours	Hours of sleep before the study session
📖 study_hours	Planned/studied hours
⏸️ break_minutes	Time spent taking breaks
📱 phone_hours	Phone usage during the study period
🧘 stress_level	Self-reported stress level
☕ caffeine	Number of caffeine servings
📊 previous_productivity	Productivity score from a previous session

Based on these inputs, the model predicts:

Low
Medium
High
🧠 Machine Learning

The main machine learning model used in this project is:

🌲 Random Forest Classifier

Random Forest was used as the main classification model because it can work with multiple numerical features and capture non-linear relationships between them.

The project also includes experimentation with other classification models for comparison, including:

Decision Tree
Logistic Regression

The models are evaluated using common classification metrics such as:

Accuracy
Precision
Recall
F1-score
Confusion Matrix
📊 Exploratory Data Analysis

Before training the model, the dataset was explored using:

Dataset shape and information
Missing-value checks
Descriptive statistics
Productivity class distribution
Box plots
Correlation analysis
Feature relationships

Some of the visualizations are included in:

notebooks/eda.ipynb
🌳 Feature Importance

The Random Forest model also allows us to look at the relative importance of the input features.

This helps us understand which features the model relied on more while making its predictions.

A feature-importance visualization is included in the notebook.

Feature importance shows how the model used the available features. It should not be interpreted as proof that one factor directly causes productivity.

🌐 Streamlit App

The project includes a simple web interface built using Streamlit.

Instead of running Python code manually, users can enter their study-session information using sliders.

The app then displays:

Your Inputs
     ↓
Random Forest Model
     ↓
Predicted Productivity
     ↓
Model Confidence
🚀 Run the app

First install the required packages:

pip install -r requirements.txt

Then start Streamlit:

streamlit run app.py

The app will normally open at:

http://localhost:8501
🗂️ Project Structure
study-mood-ai/
│
├── data/
│   └── study_sessions.csv
│
├── notebooks/
│   ├── eda.ipynb
│   └── model_evaluation.ipynb
│
├── src/
│   ├── data_generator.py
│   └── study_mood_model.pkl
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
🛠️ Technologies Used
Programming
Python
Data Handling
Pandas
NumPy
Machine Learning
Scikit-learn
Data Visualization
Matplotlib
Seaborn
Model Saving
Joblib
Deployment / Interface
Streamlit
Development
Jupyter Notebook
VS Code
Git
GitHub
🔬 Dataset

The dataset used in this project is synthetic.

It was generated specifically for this educational project using Python rather than collected from real students.

The generated dataset contains study-session records with the features described above.

Because the data is synthetic:

The predictions from this project should not be treated as a scientifically validated measurement of a person's actual productivity.

The project is intended for:

Learning
Experimentation
Understanding ML workflows
Portfolio development

and not for making real psychological, academic, or health-related decisions.

🧪 Project Workflow

Here is the complete workflow followed in this project:

Day 1 — Project Setup
Created the GitHub repository
Created the Python environment
Installed required libraries
Generated the synthetic dataset
Added Git/GitHub version control
Day 2 — Exploratory Data Analysis
Loaded the dataset
Checked the data structure
Checked missing values
Calculated descriptive statistics
Created visualizations
Studied feature correlations
Day 3 — First ML Model
Separated features and target
Created training and testing sets
Trained a Random Forest classifier
Generated predictions
Calculated accuracy
Examined feature importance
Saved the trained model using Joblib
Day 4 — Model Comparison
Trained additional classification models
Compared model performance
Used classification metrics
Examined the confusion matrix
Day 5 — Prediction Pipeline
Connected the trained model to user-input data
Prepared the prediction workflow
Tested predictions with new inputs
Day 6 — Streamlit App
Created the web interface
Added interactive input sliders
Added prediction functionality
Added model-confidence display
Added a note explaining the synthetic dataset
Day 7 — GitHub & Documentation
Organized the repository
Added project documentation
Added requirements.txt
Improved the README
Prepared the project for sharing
📌 What I Learned

This project helped me understand that building an ML project is much more than training a model.

Through this project, I practiced:

Python
  ↓
Data Generation
  ↓
Data Cleaning & Exploration
  ↓
Visualization
  ↓
Feature Selection
  ↓
Train/Test Split
  ↓
Machine Learning
  ↓
Model Evaluation
  ↓
Model Saving
  ↓
Prediction
  ↓
Streamlit
  ↓
Git & GitHub

Most importantly, I got to see how all these pieces connect together in one project.

🚧 Limitations

There are a few important limitations to keep in mind:

The dataset is synthetic.
The model has not been validated on a real-world population.
The features are simplified representations of study sessions.
Model confidence should not be interpreted as certainty.
Predictions are intended for educational experimentation.

So this project is best viewed as a learning and portfolio project, not a real productivity assessment system.

🔮 Future Improvements

There are several ways this project could be developed further:

📊 Better Data

Use a larger and more realistic dataset collected from actual study sessions.

🤖 Model Improvements

Try additional machine learning algorithms and tune their hyperparameters.

📈 Better Evaluation

Use cross-validation and more robust evaluation methods.

👤 Personalization

Allow users to keep track of previous sessions and analyze their own trends.

📱 Better UI

Create a more polished dashboard with charts and historical productivity data.

☁️ Deployment

Deploy the Streamlit application so it can be accessed online.

💭 Why I Made This

I wanted to build something small enough to actually finish, but complete enough to teach me what a real ML workflow looks like.

Instead of creating a project that only says:

"Model trained successfully ✅"

I wanted to understand what happens from data → model → prediction → application.

And honestly, making a project about study productivity while being a student felt a little too relatable. 😅

👩‍💻 Project Status

Status: ✅ Completed as a learning/portfolio project

The current version includes:

✅ Synthetic dataset generation
✅ Exploratory data analysis
✅ Machine learning classification
✅ Model evaluation
✅ Feature importance analysis
✅ Saved trained model
✅ Streamlit interface
✅ GitHub version control
✅ Project documentation
⭐ Try It

Clone the repository:

git clone https://github.com/Varu095/study-moody

Move into the project:

cd study-mood-ai

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Then open the local Streamlit URL shown in the terminal.

📚 Final Note

This project started as a small experiment to practice machine learning.

It turned into a complete mini-project covering:

Data → EDA → ML → Evaluation → Deployment → GitHub

And that's exactly what I wanted to learn from it. 🚀

Built while learning, experimenting, debugging, and occasionally procrastinating. 😅

