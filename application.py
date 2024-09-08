# from flask import Flask,request,render_template
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import CustomData,PredictPipeline
 

# application = Flask(__name__)
# app = application

# # Route for a home page

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():

#     if request.method=="GET":
#         return render_template('home.html')
    
#     else:
#         data = CustomData(
#             gender = request.form.get('gender'),
#             race_ethnicity = request.form.get('ethnicity'),
#             parental_level_of_education = request.form.get('parental_level_of_education'),
#             lunch = request.form.get('lunch'),
#             test_preparation_course = request.form.get('test_preparation_course'),
#             reading_score = float(request.form.get("reading_score")),
#             writing_score = float(request.form.get("writing_score"))

#         )

#         pred_df = data.get_data_as_data_frame()
#         print(pred_df)

#         predict_pipeline= PredictPipeline()
#         results= predict_pipeline.predict(pred_df)
#         return render_template('home.html',results=results[0])
    
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')

import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Set up the Streamlit interface
st.title("Student Performance Prediction")
st.write("This app predicts student performance based on several factors.")

# Input fields using Streamlit (no default values)
gender = st.selectbox("Gender", options=["", "male", "female"], index=0)
ethnicity = st.selectbox("Race/Ethnicity", options=["", "group A", "group B", "group C", "group D", "group E"], index=0)
parental_level_of_education = st.selectbox("Parental Level of Education", 
                                           options=["", "high school", "some college", "bachelor's degree", 
                                                    "master's degree", "associate's degree"], index=0)
lunch = st.selectbox("Lunch", options=["", "standard", "free/reduced"], index=0)
test_preparation_course = st.selectbox("Test Preparation Course", options=["", "none", "completed"], index=0)

# Choice to use slider or manual input
use_slider = st.checkbox("Use sliders for score input", value=True)

if use_slider:
    # Adjust the sliders to allow for two-digit floating point numbers
    reading_score = st.slider("Reading Score", min_value=0.0, max_value=100.0, value=50.0, step=0.01)
    writing_score = st.slider("Writing Score", min_value=0.0, max_value=100.0, value=50.0, step=0.01)
else:
    # Manual input fields (empty default value)
    reading_score = st.text_input("Enter Reading Score", value="")
    writing_score = st.text_input("Enter Writing Score", value="")

# Check for missing values and predict
if st.button("Predict"):
    # Validation for empty fields
    if not gender or not ethnicity or not parental_level_of_education or not lunch or not test_preparation_course:
        st.error("Please fill in all fields before making a prediction.")
    elif not reading_score or not writing_score:
        st.error("Please provide valid scores for Reading and Writing.")
    else:
        try:
            reading_score = float(reading_score)
            writing_score = float(writing_score)
            
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            st.write(pred_df)
            st.write(results)

            # Display the results
            st.success(f"The predicted score is: {results[0]}")
        except ValueError:
            st.error("Reading and Writing scores must be valid numbers.")
