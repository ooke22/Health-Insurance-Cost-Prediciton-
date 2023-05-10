import pickle
import numpy as np
import pandas as pd
import streamlit as st

model = pickle.load(open('C:/Insurance_Cost_App/GDBR_Insu_model.pkl', 'rb'))

def welcome():
    return 'Welcome'

def insurance_cost(new_data):
   new_data_as_numpy_array = np.asarray(new_data)
   new_data_reshaped = new_data_as_numpy_array.reshape(1,-1)
   prediction = model.predict(new_data_reshaped)
   print('Potential Insurance Cost is: ', prediction)
   return 'Your predicted insurance cost is: {}'.format(prediction)


def main():
    st.title('Insurance Cost Prediction')

    html_temp = """ 
    <div style = background-color:teal;padding:10px>
    <h2 style="color:white;text-align:center;">Medical Insurance Cost Prediction </h2> 
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.number_input('Age', min_value=1, max_value=100)
    bmi = st.number_input('BMI', min_value=10, max_value=90)
    children = st.number_input('Number of children', min_value = 1, max_value = 100)
    sex = st.number_input('Sex', min_value = 0, max_value=1)
    smoker = st.number_input('Smoker', min_value = 0, max_value = 1)
    region_northeast = st.number_input('Northeast Region', min_value = 0, max_value =1)
    region_northwest = st.number_input('Northwest Region', min_value = 0, max_value =1)
    region_southeast = st.number_input('Southeast Region', min_value = 0, max_value =1)
    region_southwest = st.number_input('Southwest Region', min_value = 0, max_value =1)

    ## code for prediction
    result = ""
    if st.button("Predict"):
        result = insurance_cost([age, bmi, children, sex, smoker, region_northeast, region_northwest, region_southeast, region_southwest])
    st.success(result)

if __name__ == '__main__':
    main()

# Updates:
# Change the format to make text disappear when user begins typing
# Change Sex, smoker, and region to present multiple options for users
# For ex: Sex - male or female option using appropriate st. function
# Region - Choose region: backend- if user chooses
#%%
