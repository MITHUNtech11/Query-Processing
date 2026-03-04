import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("alphabet_stock_data.csv", parse_dates=['Date'])

# Define date range
start_date = "2020-04-01"
end_date = "2020-04-30"

# Filter data between two dates
filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Create scatter plot (Volume vs Close Price)
plt.figure()
plt.scatter(filtered['Volume'], filtered['Close'])
plt.title("Trading Volume vs Closing Price (Alphabet Inc.)")
plt.xlabel("Trading Volume")
plt.ylabel("Closing Stock Price")
plt.show()