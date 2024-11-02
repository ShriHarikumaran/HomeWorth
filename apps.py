


import streamlit as st
import joblib 
import numpy as np

model=joblib.load("model_compressed.pkl")
st.set_page_config(page_title="HomeWorth", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f3f4f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .stNumberInput>div>input {
        border: 2px solid #4CAF50;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 HomeWorth: Your Instant House Price Estimator")
st.divider()

st.subheader("Get an instant estimate of your home's worth with ease!")
st.write("Fill out the following details to get a quick price estimate:")


bedrooms=st.number_input("Number of bedrooms",min_value=0,value=0,key="1")
bathrooms=st.number_input("Number of bathrooms",min_value=0,value=0,key="2")
livingarea=st.number_input("Size of Living Area",min_value=0,value=2000,key="3")
condition=st.number_input("Condiiton of a house",min_value=0,value=3,key="4")
noofschools=st.number_input("Number of schools nearby",min_value=0,value=0,key="5")
nooffloors=st.number_input("Number of floors",min_value=0,value=1,key="6")
airportdistance=st.number_input("Distance from the airport",min_value=0,value=1,key="7")
st.divider()




x=[[bedrooms,bathrooms,livingarea,condition,noofschools,nooffloors,airportdistance]]
predictionbutton=st.button("PREDICT")
if predictionbutton:
    
    x_array=np.array(x)
    prediction=model.predict(x_array)
    st.success(f"🏡 Estimated Home Price: **$ {prediction[0]:,.2f}**")
else:
    st.info("Enter the values above and click PREDICT to see the estimate.")

