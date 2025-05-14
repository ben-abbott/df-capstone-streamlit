import streamlit as st


def search_tickers(df):
    search_input = st.text_input('Search for a ticker:', '').upper()

    if search_input:
        search_df = df.loc[df['symbol'] == search_input]
    else:
        search_df = df
    return search_df
