import streamlit as st
import plotly.express as px

# top 400 sector bar chart


def create_top_stocks_sector_chart(df):
    top_stocks = df.nsmallest(400, 'overallRank')
    sector_count = top_stocks['sector'].value_counts().reset_index()
    sector_count.columns = ['Sector', 'Number of Stocks']
    fig = px.bar(
        sector_count,
        x='Sector',
        y='Number of Stocks',
        title='Top 400 by Sector',
        text='Number of Stocks',
        color='Sector'
    )
    return fig


def create_all_sector_chart(df):
    all_sector_count = df['sector'].value_counts().reset_index()
    all_sector_count.columns = ['Sector', 'Number of Stocks']
    fig = px.bar(
        all_sector_count,
        x='Sector',
        y='Number of Stocks',
        title='All Stocks by Sector',
        text='Number of Stocks',
        color='Sector'
    )
    return fig


def create_top_stocks_prices(df):
    top_stocks = df.nsmallest(400, 'overallRank')
    top_stocks_price = top_stocks[(
        top_stocks['price'] > 0) & (top_stocks['price'] < 250)]
    fig = px.histogram(
        top_stocks_price,
        x='price',
        nbins=20,
        title='Top 400 Stock Price Distribution'
    )
    return fig


def create_all_price_histogram(df):
    stock_prices = df[(df['price'] > 0) & (df['price'] < 1000)]
    fig = px.histogram(
        stock_prices,
        x='price',
        nbins=100,
        title='Price Distribution',
        opacity=0.8
    )
    return fig


def visualizations(df):
    top_stocks_by_sector = create_top_stocks_sector_chart(df)
    all_stocks_by_sector = create_all_sector_chart(df)
    top_stocks_by_price = create_top_stocks_prices(df)
    all_stocks_by_price = create_all_price_histogram(df)
    st.plotly_chart(top_stocks_by_sector)
    st.plotly_chart(all_stocks_by_sector)
    st.plotly_chart(top_stocks_by_price)
    st.plotly_chart(all_stocks_by_price)
