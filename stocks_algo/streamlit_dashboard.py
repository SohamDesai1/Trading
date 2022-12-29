import streamlit as st
import pandas as pd
import datetime
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Stock Price Screener and Analysis")
pd.set_option('max_colwidth', 400)
df = pd.DataFrame()

todays_stock, stocks, indicators = st.tabs(
    ["Stock price for Today ", "Historical Price of Stock", "Indicators"])

with todays_stock:
    st.title("Today's Price of Stock")
    stock = st.text_input("Enter a stock ticker symbol", "LT")
    Today_stock = st.button("Get Today's Price")
    today = datetime.date.today()
    if Today_stock:
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


with stocks:
    st.title("Stocks")
    stock_name = st.text_input("Enter a stock ticker symbol")
    start_date = st.date_input("Start date")
    goto_today = st.button("Get Price from start date till today")
    end_date = st.date_input("End date")
    get_stock = st.button("Get Stock Price")
    today_date = datetime.date.today() + datetime.timedelta(days=1)
    if end_date < start_date:
        st.error("Error: End date must fall after start date.")
    elif goto_today:
        end_date = today_date
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
    elif get_stock:
        df = yf.download(f"{stock}.NS", start=start_date,
                         end=end_date+datetime.timedelta(days=1), interval="15m")
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


with indicators:
    # select = st.sidebar.selectbox("Select a indicator",["aberration", "above", "above_value", "accbands", "ad", "adosc", "adx", "alma", "amat", "ao", "aobv", "apo", "aroon", "atr", "bbands","below", "below_value", "bias", "bop", "brar", "cci," "cdl_pattern", "cdl_z", "cfo", "cg", "chop","cksp", "cmf", "cmo", "coppock", "cross", "cross_value", "cti," "decay", "decreasing", "dema", "dm", "donchian", "dpo", "ebsw", "efi", "ema", "entropy", "eom", "er ","eri", "fisher", "fwma", "ha", "hilo", "hl2," "hlc3", "hma," "hwc," "hwma", "ichimoku", "increasing", "inertia", "jma", "kama", "kc", "kdj," "kst," "kurtosis", "kvo," "linreg", "log_return", "long_run," "macd"," mad", "massi", "mcgd", "median", "mfi," "midpoint", "midprice", "mom," "natr", "nvi," "obv," "ohlc4", "pdist", "percent_return", "pgo," "ppo," "psar", "psl," "pvi," "pvo," "pvol", "pvr," "pvt," "pwma", "qqe," "qstick", "quantile", "rma," "roc," "rsi," "rsx," "rvgi", "rvi," "short_run", "sinwma", "skew", "slope", "sma", "smi", "squeeze", "squeeze_pro", "ssf," "stc," "stdev", "stoch", "stochrsi", "supertrend", "swma", "t3, ""td_seq", "tema", "thermo", "tos_stdevall", "trima", "trix", "true_range", "tsi," "tsignals", "ttm_trend", "ui, ""uo, ""variance", "vhf," "vidya", "vortex", "vp, ""vwap", "vwma", "wcp," "willr", "wma," "xsignals", "zlma", "zscore"])
    
    stock_name = st.text_input("Enter a stock ticker symbol", "RELIANCE")
    category = st.selectbox("Select a category", [
        'candles', 'cycles', 'momentum', 'overlap', 'performance', 'statistics', 'trend', 'volatility', 'volume'])
    button_clicked = st.button("Get Indicators")
    if category == "candles":
        st.write("The Candles category contains the following indicators : ")
    if button_clicked:
        df = pd.DataFrame()
        df = df.ta.ticker(f"{stock_name}.NS", period="1y", asobject=True)
        df.ta.strategy(category)
        st.write(df)
