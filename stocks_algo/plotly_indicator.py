import pandas_ta as ta
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame()
df = df.ta.ticker("LT.NS", period="1y", asobject=True)

adx = df.ta.adx()

adx_25 = adx[adx['ADX_14'] < 45]
adx_25 = adx_25.reset_index()
adx_25 = adx_25.rename(columns={'index': 'Date'})
print(adx_25)

concat = pd.concat([df, adx], axis=1)

fig = go.Figure()
fig.add_trace(go.Scatter(x=concat.index, y=concat['Open'], name='Open'))
fig.add_trace(go.Scatter(x=concat.index, y=concat['Close'], name='Close'))
fig.add_trace(go.Scatter(x=adx_25['Date'], y=adx_25['ADX_14'], name='ADX_14_25_45'))
fig.show()
