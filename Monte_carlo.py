import pandas as pd
import numpy as np
import os

# -----------------------------
# Load daily log returns
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
returns_file = os.path.join(current_dir, 'daily_log_returns.csv')

returns = pd.read_csv(returns_file, index_col='Date', parse_dates=True)

print("✅ Daily returns loaded")
print(returns.head())

# -----------------------------
# Portfolio configuration
# -----------------------------
num_simulations = 10000
num_days = 252  # trading days in 1 year
initial_investment = 1_000_000  # ₹10 lakh

mean_returns = returns.mean()
cov_matrix = returns.cov()

num_assets = len(mean_returns)
weights = np.array([1 / num_assets] * num_assets)

# -----------------------------
# Monte Carlo Simulation
# -----------------------------
portfolio_results = np.zeros(num_simulations)

for i in range(num_simulations):
    simulated_returns = np.random.multivariate_normal(
        mean_returns,
        cov_matrix,
        num_days
    )

    portfolio_daily_returns = simulated_returns.dot(weights)
    portfolio_value = initial_investment * np.exp(np.cumsum(portfolio_daily_returns))
    portfolio_results[i] = portfolio_value[-1]

# -----------------------------
# Save Monte Carlo results
# -----------------------------
mc_file = os.path.join(current_dir, 'monte_carlo_results.csv')
pd.DataFrame(portfolio_results, columns=['Final_Portfolio_Value']).to_csv(mc_file, index=False)

print("✅ Monte Carlo simulation completed")
print("Sample final portfolio values:")
print(portfolio_results[:5])

# -----------------------------
# Value at Risk (VaR)
# -----------------------------
var_95 = np.percentile(portfolio_results, 5)
var_99 = np.percentile(portfolio_results, 1)

var_df = pd.DataFrame({
    'Metric': ['Initial Investment', 'VaR 95%', 'VaR 99%'],
    'Value': [initial_investment, var_95, var_99]
})

var_file = os.path.join(current_dir, 'var_results.csv')
var_df.to_csv(var_file, index=False)

print("\n📉 Value at Risk Results:")
print(var_df)
