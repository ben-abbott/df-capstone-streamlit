import streamlit as st
from load import load_data

df = load_data()

# Set the title of the app
st.title("My First Streamlit App")
# Display a simple message
st.write("Hello, Streamlit!")

st.dataframe(df)
