import pandas as pd
import requests
import time
from datetime import datetime


def DatetoTimestamp(date):
    time_tuple = date.timetuple()
    timestamp = round(time.mktime(time_tuple))
    return timestamp


def TimestamptoDate(timestamp):
    return datetime.fromtimestamp(timestamp)


start = DatetoTimestamp(datetime(2022, 12, 8))
end = DatetoTimestamp(datetime.today())

url = "https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol=RELIANCE&resolution=15&from=" + \
    str(start)+"&to="+str(end)+"&countback=2&currencyCode=INR"

res = requests.get(url=url).json()

data = pd.DataFrame(res)
print(data)
