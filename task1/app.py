import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained Random Forest Regressor model
model = joblib.load('random_forest_regressor_model.pkl')

# Add a background image with reduced opacity
page_bg_img = '''
<style>
body {
background-image: url("https://housing.com/news/wp-content/uploads/2022/11/shutterstock_1715891752-1200x700-compressed.jpg");
background-size: cover;
background-attachment: fixed;
opacity: 0.7;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the app
st.title('House Price Prediction App')

# Instructions
st.write('Enter the required input values for the model prediction:')

# Create columns for side-by-side input fields
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)

# Input fields for user to enter data
with col1:
    rooms = st.number_input('Rooms', value=0, step=1)
with col2:
    postcode = st.number_input('Postcode', value=0, step=1)
with col3:
    bedroom2 = st.number_input('Bedroom2', value=0, step=1)
with col4:
    bathroom = st.number_input('Bathroom', value=0, step=1)
with col5:
    car = st.number_input('Car', value=0, step=1)
with col6:
    landsize = st.number_input('Landsize', value=0, step=1)
with col7:
    buildingarea = st.number_input('BuildingArea', value=0, step=1)
with col8:
    yearbuilt = st.number_input('YearBuilt', value=0, step=1)
with col9:
    councilarea = st.number_input('CouncilArea', value=0, step=1)

# Assume regionname is a constant or derived in some way
regionname = 0

# Button to make prediction
if st.button('Predict'):
    # Prepare the input data for the model
    input_data = np.array([[rooms, postcode, bedroom2, bathroom, car, landsize, buildingarea, yearbuilt, councilarea, regionname]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the prediction result
    st.success(f'Predicted Price: ${prediction[0]:,.2f}')


