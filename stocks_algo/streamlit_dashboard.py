from math import floor
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

st.header("S&P BSE SENSEX")
today = datetime.date.today()
sensex = yf.download("^BSESN",start=today, interval="5m")
sensex_current = floor(sensex['Close'].iloc[-1])
st.write(f"Current Price: {sensex_current}")
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[
                            0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "bar"}]])
fig.update_xaxes(rangeslider_visible=False)
fig.add_trace(go.Candlestick(x=sensex.index, open=sensex['Open'], high=sensex['High'],
                        low=sensex['Low'], close=sensex['Close'], name='market data'), row=1, col=1)
st.plotly_chart(fig, use_container_width=True)


st.header("NIFTY 50")
nifty = yf.download("^NSEI",start=today, interval="5m")
nifty_current = floor(nifty['Close'].iloc[-1])
st.write(f"Current Price: {nifty_current}")
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[
                            0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "bar"}]])
fig.update_xaxes(rangeslider_visible=False)
fig.add_trace(go.Candlestick(x=nifty.index, open=nifty['Open'], high=nifty['High'],
                        low=nifty['Low'], close=nifty['Close'], name='market data'), row=1, col=1)  
st.plotly_chart(fig, use_container_width=True)

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
        df['% Change'] = df['Close'].pct_change()*100
        df['% Change'] = df['% Change'].round(2)
        st.write(df)
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[
                            0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "bar"}]])
        fig.update_xaxes(rangeslider_visible=False)
        fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                      low=df['Low'], close=df['Close'], name='market data'), row=1, col=1)
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
    candles = "2crows","3blackcrows","3inside","3linestrike","3outside","3starsinsouth","3whitesoldiers","abandonedbaby","advanceblock","belthold","breakaway","closingmarubozu","concealbabyswall","counterattack","darkcloudcover","doji","dojistar","dragonflydoji","engulfing","eveningdojistar","eveningstar","gapsidesidewhite","gravestonedoji","hammer","hangingman","harami","haramicross","highwave","hikkake","hikkakemod","homingpigeon","identical3crows","inneck","inside","invertedhammer","kicking","kickingbylength","ladderbottom","longleggeddoji","longline","marubozu","matchinglow","mathold","morningdojistar","morningstar","onneck","piercing","rickshawman","risefall3methods","separatinglines","shootingstar","shortline","spinningtop","stalledpattern","sticksandwich","takuri","tasukigap","thrusting","tristar","unique3river","upsidegap2crows","xsidegap3methods","Heikin-Ashi: ha","Z Score: cdl_z"

    cycles = "Even Better Sinewave: ebsw"

    momentum = "Awesome Oscillator: ao","Absolute Price Oscillator: apo","Bias: bias","Balance of Power: bop","BRAR: brar","Commodity Channel Index: cci","Chande Forecast Oscillator: cfo","Center of Gravity: cg","Chande Momentum Oscillator: cmo","Coppock Curve: coppock","Correlation Trend Indicator: cti","Directional Movement: dm","Efficiency Ratio: er","Elder Ray Index: eri","Fisher Transform: fisher","Inertia: inertia","KDJ: kdj","KST Oscillator: kst","Moving Average Convergence Divergence: macd","Momentum: mom","Pretty Good Oscillator: pgo","Percentage Price Oscillator: ppo","Psychological Line: psl","Percentage Volume Oscillator: pvo","Quantitative Qualitative Estimation: qqe","Rate of Change: roc","Relative Strength Index: rsi","Relative Strength Xtra: rsx","Relative Vigor Index: rvgi","Schaff Trend Cycle: stc","Slope: slope","SMI Ergodic smi","Squeeze: squeeze","Squeeze Pro: squeeze_pro","Stochastic Oscillator: stoch","Stochastic RSI: stochrsi","TD Sequential: td_seq","Trix: trix","True strength index: tsi","Ultimate Oscillator: uo","Williams %R: willr"

    overlap = "Arnaud Legoux Moving Average: alma","Double Exponential Moving Average: dema","Exponential Moving Average: ema","Fibonacci's Weighted Moving Average: fwma","Gann High-Low Activator: hilo","High-Low Average: hl2","High-Low-Close Average: hlc3","Commonly known as 'Typical Price' in Technical Analysis literature","Hull Exponential Moving Average: hma","Holt-Winter Moving Average: hwma","Ichimoku Kinkō Hyō: ichimoku","Jurik Moving Average: jma","Kaufman's Adaptive Moving Average: kama","Linear Regression: linreg","McGinley Dynamic: mcgd","Midpoint: midpoint","Midprice: midprice","Open-High-Low-Close Average: ohlc4","Pascal's Weighted Moving Average: pwma","WildeR's Moving Average: rma","Sine Weighted Moving Average: sinwma","Simple Moving Average: sma","Ehler's Super Smoother Filter: ssf","Supertrend: supertrend","Symmetric Weighted Moving Average: swma","T3 Moving Average: t3","Triple Exponential Moving Average: tema","Triangular Moving Average: trima","Variable Index Dynamic Average: vidya","Volume Weighted Average Price: vwap","Requires the DataFrame index to be a DatetimeIndex","Volume Weighted Moving Average: vwma","Weighted Closing Price: wcp","Weighted Moving Average: wma","Zero Lag Moving Average: zlma"

    performance = "Draw Down: drawdown","Log Return: log_return","Percent Return: percent_return"

    statistics = "Entropy: entropy","Kurtosis: kurtosis","Mean Absolute Deviation: mad","Median: median","Quantile: quantile","Skew: skew","Standard Deviation: stdev","Think or Swim Standard Deviation All: tos_stdevall","Variance: variance","Z Score: zscore"

    trend = "Average Directional Movement Index: adx","Archer Moving Averages Trends: amat","Aroon & Aroon Oscillator: aroon","Choppiness Index: chop","Chande Kroll Stop: cksp","Decay: decay","Decreasing: decreasing","Detrended Price Oscillator: dpo","Increasing: increasing","Long Run: long_run","Parabolic Stop and Reverse: psar","Q Stick: qstick","Short Run: short_run","Trend Signals: tsignals","TTM Trend: ttm_trend","Vertical Horizontal Filter: vhf","Vortex: vortex","Cross Signals: xsignals"

    utility = "Above: above","Above Value: above_value","Below: below","Below Value: below_value","Cross: cross"

    volatility = "Aberration: aberration","Acceleration Bands: accbands","Average True Range: atr","Bollinger Bands: bbands","Donchian Channel: donchian","Holt-Winter Channel: hwc","Keltner Channel: kc","Mass Index: massi","Normalized Average True Range: natr","Price Distance: pdist","Relative Volatility Index: rvi","Elder's Thermometer: thermo","True Range: true_range","Ulcer Index: ui"

    volume ="Accumulation/Distribution Index: ad","Accumulation/Distribution Oscillator: adosc","Archer On-Balance Volume: aobv","Chaikin Money Flow: cmf","Elder's Force Index: efi","Ease of Movement: eom","Klinger Volume Oscillator: kvo","Money Flow Index: mfi","Negative Volume Index: nvi","On-Balance Volume: obv","Positive Volume Index: pvi","Price-Volume: pvol","Price Volume Rank: pvr","Price Volume Trend: pvt","Volume Profile: vp"

    stock_name = st.text_input("Enter a stock ticker symbol", "RELIANCE")
    category = st.selectbox("Select a category", [
        'candles', 'cycles', 'momentum', 'overlap', 'performance', 'statistics', 'trend', 'volatility', 'volume'])
    button_clicked = st.button("Get Indicators")
    st.write(f"These are the following indicators available in {category} category")
    if category == "candles":
        st.write(candles)
    elif category == "cycles":
        st.write(cycles)
    elif category == "momentum":
        st.write(momentum)
    elif category == "overlap":
        st.write(overlap)
    elif category == "performance":
        st.write(performance)
    elif category == "statistics":
        st.write(statistics)
    elif category == "trend":
        st.write(trend)
    elif category == "volatility":
        st.write(volatility)
    elif category == "volume":
        st.write(volume)
        
    if button_clicked:
        df1 = pd.DataFrame()
        df1 = df.ta.ticker(f"{stock_name}.NS", period="1y", asobject=True)
        df1.ta.strategy(category)
        df1 = df1.drop(columns=['Stock Splits', 'Dividends'])
        st.write(df1)
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[
                            0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "bar"}]])
        fig.update_xaxes(rangeslider_visible=False)
        fig.add_trace(go.Candlestick(x=df1.index, open=df1['Open'], high=df1['High'],
                      low=df1['Low'], close=df1['Close'], name='market data'), row=1, col=1)
        # bar chart
        fig.add_trace(
            go.Bar(x=df1.index, y=df1['Volume'], name='Volume'), row=2, col=1)

        st.plotly_chart(fig, use_container_width=True)
