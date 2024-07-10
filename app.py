import os
import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler


# Set page configuration
st.set_page_config(page_title="Diabetes Detector",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
# working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

# diabetes_model = pickle.load(open(f'{working_dir}/model.sav', 'rb'))
diabetes_model = pickle.load(open('model.sav', 'rb'))

# page title
st.title('Diabetes Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:

  options = ['Male', 'Female', 'Other']

  Gender = st.selectbox('Gender', options)
  
  if Gender=="Male":
    Gender=0
  elif Gender=="Female":
    Gender=1
  else:
    Gender=2

with col2:
  
  Age = st.text_input('Age')
  
  if Age: 
    
    try:
      Age = float(Age)
    except ValueError:
      # raise ValueError("Age field must be a valid number")
      st.error("Invalid Input")
    
with col3:
  
  options = ['Yes', 'No']

  Hypertension = int(st.selectbox('Hypertension', options) == 'Yes')

with col1:
  
  options = ['Yes', 'No']

  HeartDisease = int(st.selectbox('Heart Disease', options) == "Yes")

with col2:
  
  options = ['No Info', 'never','former','current','not current','ever']

  SmokingHistory = st.selectbox('Smoking History', options)
  
  if SmokingHistory:
    SmokingHistory= options.index(SmokingHistory)
       

with col3:
  
  BMIValue = st.text_input('BMI value')

  if BMIValue:
    
    try:
      BMIValue = float(BMIValue)
    except ValueError:
      # raise ValueError("Age field must be a valid number")
      st.error("Invalid Input")

with col1:
  
  HbA1c_Level= st.text_input('HbA1c Level')
  
  if HbA1c_Level:
    
    try:
      HbA1c_Level = float(HbA1c_Level)
    except ValueError:
      # raise ValueError("HbA1c Level field must be a valid number")
      st.error("Invalid Input")
with col2:
  
  BloodGlucoseLevel = st.text_input('Blood Glucose Level')
  if BloodGlucoseLevel:
    
    try:
      BloodGlucoseLevel = float(BloodGlucoseLevel)
    except ValueError:
      # raise ValueError("Blood Glucose Level field must be a valid number")
      st.error("Invalid input")

# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

scaler = pickle.load(open('scaler1.pkl', 'rb'))

def prediction(input_data):
  input_data_as_numpy_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
  std_data = scaler.transform(input_data_reshaped)
  prediction = diabetes_model.predict(std_data)
  if (prediction[0] == 0):
    return 0
  else:
    return 1



if st.button('Diabetes Test Result'):

  
  user_input = [Gender, Age, Hypertension, HeartDisease, SmokingHistory,
                      BMIValue, HbA1c_Level, BloodGlucoseLevel]
  print(user_input)
  
  diab_prediction = prediction([user_input])

  
  if diab_prediction == 1:
      
      diab_diagnosis = 'The person is diabetic'
  
  else:
      
       diab_diagnosis = 'The person is not diabetic'

  st.success(diab_diagnosis)

