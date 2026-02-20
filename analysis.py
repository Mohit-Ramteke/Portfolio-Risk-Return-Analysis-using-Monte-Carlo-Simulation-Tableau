import pandas as pd
import numpy as np
import os

# -----------------------------
# Load clean prices
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
price_file = os.path.join(current_dir, 'clean_prices.csv')

prices = pd.read_csv(price_file, index_col='Date', parse_dates=True)

print("✅ Clean prices loaded")
print(prices.head())

# -----------------------------
# Daily Log Returns
# -----------------------------
log_returns = np.log(prices / prices.shift(1))
log_returns.dropna(inplace=True)

log_returns_file = os.path.join(current_dir, 'daily_log_returns.csv')
log_returns.to_csv(log_returns_file)

print("✅ Daily log returns saved")

# -----------------------------
# Rolling Volatility (30-day)
# -----------------------------
rolling_volatility = log_returns.rolling(window=30).std()

volatility_file = os.path.join(current_dir, 'rolling_volatility_30d.csv')
rolling_volatility.to_csv(volatility_file)

print("✅ Rolling volatility saved")

# -----------------------------
# Correlation Matrix
# -----------------------------
correlation_matrix = log_returns.corr()

correlation_file = os.path.join(current_dir, 'correlation_matrix.csv')
correlation_matrix.to_csv(correlation_file)

print("✅ Correlation matrix saved")

print("\nCorrelation Matrix:")
print(correlation_matrix)
