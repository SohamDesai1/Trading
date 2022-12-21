import pandas_ta as ta
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame()
df = df.ta.ticker("LT.NS", period="1y", asobject=True)

adx = df.ta.adx()

adx_25 = adx[adx['ADX_14'] < 45]
adx_25 = adx_25.reset_index()
adx_25 = adx_25.rename(columns={'index': 'Date'})
# print(adx_25)

rsi = df.ta.rsi()
print(rsi)

concat = pd.concat([df, rsi], axis=1)

fig = go.Figure() 
# enlarge candlesticks
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20), height=600)
# show candlesticks
fig.add_trace(go.Candlestick(x=concat.index, open=concat['Open'], high=concat['High'], low=concat['Low'], close=concat['Close'], name='market data'))
# show rsi 
fig.add_trace(go.Scatter(x=concat.index, y=concat['RSI_14'], name='RSI_14'))
fig.show()
