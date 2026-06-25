import streamlit as st
import pandas as pd
# import your ML libraries (sklearn, xgboost, etc.)

st.title("🎬 Box Office Revenue Predictor")

# You would load your pre-trained model here or train a quick one
df = pd.read_csv("boxoffice (1).csv")

st.write("Enter movie details to predict revenue:")
budget = st.number_input("Movie Budget ($)")
# ... add other inputs like genres, release days, etc.

if st.button("Predict Revenue"):
    # Make prediction using your model
    st.success(f"Predicted Revenue: $...")