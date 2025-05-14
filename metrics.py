import streamlit as st


def get_stock_count(df):
    return df['symbol'].nunique()


def get_avg_price(df):
    return round(df['price'].mean(), 2)


def get_highest_roc(df):
    highest_roc = df[df['rocRank'] == df['rocRank'].min()]
    # Chatgpt suggested .values as I was getting an error
    try:
        highest_roc_tick = highest_roc['symbol'].values[0]
    except Exception as e:
        print(f'error when getting highest roc ticker: {e}')
        return 'N/A'
    return highest_roc_tick


def get_highest_yield(df):
    highest_yield = df[df['yieldRank'] == df['rocRank'].min()]
    try:
        highest_yield_tick = highest_yield['symbol'].values[0]
    except Exception as e:
        print(f'error when getting highest yield ticker: {e}')
        return 'N/A'
    return highest_yield_tick


def display_metrics(df):
    stock_count = get_stock_count(df)
    mean_price = get_avg_price(df)
    highest_roc = get_highest_roc(df)
    highest_yield = get_highest_yield(df)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Number of Stocks", value=stock_count)
    with col2:
        st.metric(label="Average Price ($)", value=mean_price)
    with col3:
        st.metric(label="Highest Return", value=highest_roc)
    with col4:
        st.metric(label="Highest Yield", value=highest_yield)
