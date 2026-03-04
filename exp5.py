import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define stock ticker
ticker = "GOOGL"

# Define date range
start_date = "2022-01-01"
end_date = "2022-03-31"

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Plot trading volume as bar chart
plt.figure()
plt.bar(data.index, data['Volume'])
plt.title("Alphabet Inc. Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)
plt.show()