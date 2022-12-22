import pandas_ta as ta
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.DataFrame()
df = df.ta.ticker("LT.NS", period="1y")

adx = df.ta.adx()

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.7, 0.3], specs=[[{"type": "candlestick"}], [{"type": "scatter"}]])

fig.update_xaxes(rangeslider_visible=False)  
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='market data'), row=1, col=1)

fig.add_trace(go.Scatter(x=adx.index, y=adx['ADX_14'],line={"color":"black"}, name='ADX_14'), row=2, col=1)
fig.add_trace(go.Scatter(x=adx.index, y=adx['ADX_14'].where(adx["ADX_14"]<25),line={"color":"dark green"}, name='ADX_14'), row=2, col=1)
fig.add_trace(go.Scatter(x=adx.index, y=adx['ADX_14'].where(adx["ADX_14"]>45),line={"color":"red"}, name='ADX_14'), row=2, col=1)

# add a horizontal line in adx subplot
fig.add_shape(type="line", x0=adx.index[0], y0=25, x1=adx.index[-1], y1=25, line=dict(color="dark green", width=1), row=2, col=1)

fig.show()
