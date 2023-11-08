import yfinance as yf
import matplotlib.pyplot as plt

def trading_bot(symbol):
    # Fetch historical data
    data = yf.download(symbol, start='2022-01-01', end='2022-12-31')

    # Initialize variables
    buy_price = 0
    sell_price = 0
    portfolio = []
    buy_tickers = []
    sell_tickers = []

    # Iterate over each day
    for i in range(1, len(data)):
        current_price = data['Close'][i]
        previous_price = data['Close'][i - 1]
        change_percent = (current_price - previous_price) / previous_price * 100

        # Buy if price goes down
        if change_percent < 0 and buy_price == 0:
            buy_price = current_price
            buy_tickers.append(i)

        # Sell if price goes up by 5%
        elif change_percent >= 5 and buy_price != 0:
            sell_price = current_price
            sell_tickers.append(i)
            portfolio.append(sell_price - buy_price)
            buy_price = 0

    # Plot buy and sell tickers
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'])
    plt.scatter(data.index[buy_tickers], data['Close'][buy_tickers], marker='^', color='green', label='Buy')
    plt.scatter(data.index[sell_tickers], data['Close'][sell_tickers], marker='v', color='red', label='Sell')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Trading Bot')
    plt.legend()
    plt.show()

    # Calculate total profit
    total_profit = sum(portfolio)
    print(f'Total Profit: {total_profit:.2f}')

# Example usage
symbol = 'AAPL'
trading_bot(symbol)
