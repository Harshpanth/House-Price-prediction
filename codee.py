import sys
sys.path.insert(0, r'd:\coding\ML project\.venv\house_price_model.jb')
import os
import pandas as pd
import streamlit as st
import joblib

# Load model with full path
model_path = os.path.join(os.path.dirname(__file__), 'house_price_model.jb')
if not os.path.exists(model_path):
    model_path = os.path.join(os.path.dirname(__file__), '..', 'house_price_model.jb')
if not os.path.exists(model_path):
    model_path = os.path.join(os.path.dirname(__file__), '..', 'movierecommender', 'house_price_model.jb')
if not os.path.exists(model_path):
    st.error(f"Model file not found at: {model_path}")
    st.stop()
model = joblib.load(model_path)

st.title("House Price Prediction")
st.write("Enter the Details Below to predict the House Price")

inputs=['OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
       'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
       'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
       'CentralAir']

input_data = {}
for features in inputs:
    if features == 'CentralAir':
        input_data[features] = st.selectbox(f"{features}", options=['Yes','No'], index=0)
    else:
        input_data[features] = st.number_input(
            f"{features}",
            value=0.0,
            step=1.0 if features in ['OverallQual','FullBath','Fireplaces'] else 0.1
        )

if st.button("Predict Price"):
    input_data['CentralAir'] =1 if input_data['CentralAir'] == "Yes" else 0

    input_df = pd.DataFrame([input_data],columns=inputs)

    predictions = model.predict(input_df)
    st.success(f"Predicted House Price: ${predictions[0]:,.2f}") 