import streamlit as st
from load import load_data
from metrics import display_metrics

df = load_data()

# Set the title of the app
st.title("My First Streamlit App")
# Display a simple message
st.write("Hello, Streamlit!")

display_metrics(df)


st.dataframe(df)
