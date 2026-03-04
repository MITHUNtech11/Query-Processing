import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define stock ticker
ticker = "GOOGL"

# Define date range
start_date = "2022-01-01"
end_date = "2022-12-31"

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Plot closing price
plt.figure()
plt.plot(data.index, data['Close'])
plt.title("Alphabet Inc. Stock Price")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.xticks(rotation=45)
plt.show()