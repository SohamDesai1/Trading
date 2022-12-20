import pandas_ta as ta
import pandas as pd
import matplotlib.pyplot as plt

stock = input("Enter the stock ticker: ")
period = input("Enter the period: ")
df = pd.DataFrame()
df = df.ta.ticker(stock, period=period)

print("These are the following categories of indicators:")
print(df.ta.categories)

input1 = input("Enter the category of indicators you want to see: ")

cat_list = input1.split(",")
for i in cat_list:
    df.ta.strategy(i)

print(df)
# show all the indicators in the category
print(df.ta.indicators())
# plot df with matplotlib
plt.figure(figsize=(16, 9))
plt.plot(df.index, df['Close'], label='Close Price history')
plt.show()
