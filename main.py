import streamlit as st
from load import load_data
from metrics import display_metrics
from visualizations import visualizations
from filter import apply_filter
from search import search_tickers


def main():
    df = load_data()

    # Set the title of the app
    st.title("Digital Futures Capstone Project")
    # Display a simple message
    st.write("Exploratory look into the stock selection formula in 'The Little Book That Beats The Market'.")

    filtered_df = apply_filter(df)

    display_metrics(filtered_df)

    visualizations(filtered_df)

    search_df = search_tickers(df)

    st.dataframe(search_df)


if __name__ == '__main__':
    main()
