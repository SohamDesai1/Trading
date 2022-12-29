import streamlit as st
import pandas as pd
import datetime
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.sidebar.title("Stock Price App")
stock = st.sidebar.text_input("Enter a stock ticker symbol", "LT")
Today_stock = st.sidebar.button("Get Today's Price")
pd.set_option('max_colwidth', 400)
df = pd.DataFrame()
start_date = st.sidebar.date_input("Start date")
today = datetime.date.today()
end_date = st.sidebar.date_input("End date")
today_date = datetime.date.today() + datetime.timedelta(days=1)
goto_today = st.sidebar.button("Go to Today")
if goto_today:
    end_date = today_date

if end_date < start_date:
    st.error("Error: End date must fall after start date.")

elif Today_stock:
    start_date = today
    df = yf.download(f"{stock}.NS", start=start_date, interval="2m")
    # add percentage change column
    df['% Change'] = df['Close'].pct_change()*100
    df['% Change'] = df['% Change'].round(2)
    st.write(df)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[
                        0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "bar"}]])
    fig.update_xaxes(rangeslider_visible=False)
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                  low=df['Low'], close=df['Close'], name='market data'), row=1, col=1)
    # bar chart
    fig.add_trace(
        go.Bar(x=df.index, y=df['Volume'], name='Volume'), row=2, col=1)

    st.plotly_chart(fig, use_container_width=True)


elif start_date:
    df = yf.download(f"{stock}.NS", start=start_date,
                     end=end_date, interval="15m")
    df.style.set_properties(**{'text-align': 'left'})
    st.write(df)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[
                        0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "bar"}]])
    fig.update_xaxes(rangeslider_visible=False)
    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=["sat", "mon"]),
            dict(pattern='hour', bounds=[16, 9])
        ]
    )

    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                  low=df['Low'], close=df['Close'], name='market data'), row=1, col=1)
    # bar chart
    fig.add_trace(
        go.Bar(x=df.index, y=df['Volume'], name='Volume'), row=2, col=1)

    st.plotly_chart(fig, use_container_width=True)
