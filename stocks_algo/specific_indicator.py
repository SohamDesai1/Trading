import pandas_ta as ta
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df = df.ta.ticker("LT.NS", period="1y", asobject=True)
print(df)

adx = df.ta.adx()

concat = pd.concat([df, adx], axis=1)
print(concat)

plt.figure(figsize=(16, 9))
plt.title('LT.NS')
plt.plot(concat.index, concat['Open'], label='Open')
plt.plot(concat.index, concat['Close'], label='Close')
plt.plot(concat.index, concat['ADX_14'], label='ADX_14')
plt.legend(loc='upper left')
plt.show()

