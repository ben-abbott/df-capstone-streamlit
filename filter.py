import streamlit as st


def add_exchange_filter(df):
    return st.sidebar.multiselect(
        "Select Exchange",
        options=sorted(df['Exchange'].unique()),
        default=sorted(df['Exchange'].unique())
    )


def filtered_df(df, exchange_filter):
    return df[df['Exchange'].isin(exchange_filter)]


def apply_filter(df):
    st.sidebar.header('Filters')
    exchange_filter = add_exchange_filter(df)
    return filtered_df(df, exchange_filter)
