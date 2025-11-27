import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime

# Load trained model
model = pickle.load(open('car_price_model.pkl', 'rb'))

# App settings
st.set_page_config(page_title="Used Car Price Estimator", page_icon="🚗", layout="centered")
st.title("🚗 Used Car Price Estimator")
st.markdown("### Estimate your car's resale value instantly!")

# Sidebar inputs
st.sidebar.header("Enter Car Details")

current_year = datetime.datetime.now().year
brand = st.sidebar.selectbox("Brand", [
    "Maruti", "Hyundai", "Tata", "Honda", "Mahindra", "Toyota", "Ford",
    "Renault", "Kia", "Volkswagen", "Skoda", "Chevrolet", "BMW", "Audi",
    "Mercedes-Benz", "Nissan", "Jeep", "MG", "Fiat", "Volvo", "Jaguar"
])
year = st.sidebar.slider("Year of Manufacture", 2000, current_year, 2018)
km_driven = st.sidebar.number_input("Kilometers Driven", 0, 300000, 30000)
fuel = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.sidebar.selectbox("Number of Previous Owners", [1, 2, 3, 4])

# Derived features
car_age = current_year - year
avg_engine = 1500 if brand not in ['BMW', 'Audi', 'Mercedes-Benz', 'Jaguar'] else 2000
avg_power = 100 if brand not in ['BMW', 'Audi', 'Mercedes-Benz', 'Jaguar'] else 180

# Prepare input dataframe for the model
input_data = pd.DataFrame(np.zeros((1, len(model.feature_names_in_))), columns=model.feature_names_in_)
input_data['km_driven'] = km_driven
input_data['owner'] = owner
input_data['car_age'] = car_age
input_data['engine'] = avg_engine
input_data['max_power'] = avg_power

if f'fuel_{fuel}' in input_data.columns:
    input_data[f'fuel_{fuel}'] = 1

if 'transmission_Manual' in input_data.columns:
    input_data['transmission_Manual'] = 1 if transmission == "Manual" else 0

if f'brand_{brand}' in input_data.columns:
    input_data[f'brand_{brand}'] = 1

# Predict
if st.sidebar.button("🔍 Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"💰 Estimated Selling Price: ₹{price:,.0f}")
    st.balloons()
