## 📊 Student Performance Prediction Application
##### Access the web application: https://datascienceproject-hdmr2cecgxwmratd67brzl.streamlit.app/

#### 🎯 Project Overview
The Student Performance Prediction project is an end-to-end web application designed to predict students' academic performance based on several demographic and educational inputs. Built using Python, Streamlit, and various machine learning techniques, this project provides an easy-to-use interface for educational institutions and researchers to gain insights into student performance.

The core idea is to leverage machine learning models to predict exam scores based on multiple features such as gender, race/ethnicity, parental education, and more. This allows schools and educational experts to identify students who might need additional support, paving the way for personalized academic interventions.

#### 🛠️ Key Features
Web Application: A user-friendly interface powered by Streamlit.
Predictive Modeling: Utilizes machine learning algorithms to forecast student exam performance.
Custom Input Forms: Accepts multiple inputs like gender, race, parental education, and test preparation courses to personalize predictions.
Dynamic Scoring: Offers both slider-based and manual input options for reading and writing scores.
Real-time Results: Displays predicted results instantly after submission.

#### 🏗️ Project Architecture

data_science_project/
├── artifacts/               # Contains trained models and preprocessor objects
│   ├── model.pkl            # Serialized machine learning model
│   └── preprocessor.pkl     # Serialized preprocessor for feature scaling/encoding
├── src/                     # Main application code
│   ├── components/          # Data transformation and ingestion modules
│   │   ├── data_ingestion.py     # Data loading pipeline
│   │   └── data_transformation.py  # Data preprocessing steps
│   ├── pipeline/            # ML pipeline
│   │   ├── predict_pipeline.py    # Prediction pipeline used in the app
│   │   ├── train_pipeline.py      # Model training script
│   ├── exception.py         # Custom exception handling for better debugging
│   ├── logger.py            # Centralized logging for debugging and tracking
│   └── utils.py             # Utility functions
├── notebooks/               # Jupyter notebooks for exploratory data analysis (EDA) and model training
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb   # Exploratory Data Analysis notebook
│   ├── 2. MODEL TRAINING.ipynb            # Model Training and Evaluation notebook
├── app.py                   # Streamlit app entry point
├── requirements.txt         # Required Python libraries for the project
└── .gitignore               # Files to be ignored by version control


#### 🧠 Machine Learning Workflow

##### Exploratory Data Analysis (EDA):
Conducted through the Jupyter notebook, this step explores the dataset, analyzes trends, correlations, and outliers, and helps in feature selection.

##### Data Preprocessing:
Before training the model, the data undergoes preprocessing:

   * Categorical variables are encoded.
   * Numerical variables are scaled.
   * Missing values (if any) are handled.

#####  Model Training:
A machine learning pipeline is built using Scikit-learn, which processes the input data, applies transformations, and feeds it into a Random Forest Classifier (or other models) to train on historical data.

##### Prediction:
Once the model is trained, it is deployed into a Streamlit app. The app allows users to input data, which is preprocessed, fed into the model, and outputs a predicted student performance score.

#### 🚀 How to Run the Project
##### Prerequisites:
Python 3.8
Streamlit installed on your system

###### 1.Clone the repository
    git clone https://github.com/yourusername/student-performance-prediction.git
    cd student-performance-prediction
###### 2.Install the dependencies(pip install -r requirements.txt)
###### 3.Run the Streamlit app(streamlit run app.py)
###### 4.Access the app

#### 📊 How to Use the App

Input the Data:
Fill in the demographic details such as gender, race, parental education level, lunch type, etc.

Enter the Scores:
Choose between using sliders or manually entering the reading and writing scores.

Make a Prediction:
Click the Predict button to get the predicted score. The result will be displayed instantly.

