# Portfolio-Risk-Return-Analysis-using-Monte-Carlo-Simulation-Tableau
To analyze historical stock performance, measure risk &amp; volatility, understand correlation between assets, and simulate future portfolio values using Monte Carlo Simulation to calculate Value at Risk (VaR).


🔹 PHASE 1 — PROBLEM STATEMENT
🎯 Objective:
To analyze historical stock performance, measure risk & volatility, understand correlation between assets, and simulate future portfolio values using Monte Carlo Simulation to calculate Value at Risk (VaR).

💼 Business Use Case:
Helps investors and portfolio managers:

Understand risk exposure

Estimate worst-case losses

Make informed investment decisions

🔹 PHASE 2 — DATA COLLECTION
Step 1: Stock Price Data Extraction (Python)
We collected historical stock prices for multiple companies:

AAPL

GOOGL

JPM

MSFT

TSLA

Using Python libraries like:

yfinance

pandas

Output:
Clean historical stock price dataset.

🔹 PHASE 3 — DATA CLEANING & PREPARATION (Python)
Step 2: Cleaning & Structuring
Removed missing values

Converted date formats

Normalized stock prices

Structured dataset for time series analysis

Output File:
clean_prices.csv

🔹 PHASE 4 — FINANCIAL METRICS CALCULATION (Python)
Step 3: Daily Log Returns
Why?
Log returns are:

More statistically stable

Better for financial modeling

Formula:

log_return = ln(today_price / yesterday_price)
Output:
daily_log_returns.csv

Step 4: 30-Day Rolling Volatility
Why?
Measures risk & instability of stock prices.

Formula:

rolling_std = rolling 30-day standard deviation of log returns
Output:
rolling_volatility_30d.csv

Step 5: Correlation Matrix
Why?
Shows how assets move relative to each other.

Low correlation → good diversification

High correlation → higher portfolio risk

Output:
correlation_matrix.csv

🔹 PHASE 5 — MONTE CARLO SIMULATION (Python)
This is the heart of the project 💡

Step 6: Portfolio Simulation Logic
We simulated 10,000 future portfolio values using:

Historical returns

Volatility

Random sampling

Geometric Brownian Motion

This helps model real-world market uncertainty.

Step 7: Monte Carlo Execution
We ran:

10,000 simulations × future time horizon
Each simulation produces:
→ One possible final portfolio value

Output:
monte_carlo_results.csv

🔹 PHASE 6 — RISK METRICS (Python)
Step 8: Value at Risk (VaR) Calculation
VaR tells:

Maximum expected loss under normal market conditions.

Metric	Meaning
VaR 95%	Worst loss in 95% of scenarios
VaR 99%	Worst loss in 99% of scenarios
Output:
var_results.csv

Example:

Initial Investment: 1,000,000
VaR 95%: 738,620
VaR 99%: 625,553
Meaning:

95% confidence → portfolio will not fall below ₹738k

99% confidence → portfolio will not fall below ₹625k

🔹 PHASE 7 — DATA VISUALIZATION (TABLEAU PUBLIC)
Step 9: Import Data into Tableau
Imported:

clean_prices.csv

daily_log_returns.csv

rolling_volatility_30d.csv

correlation_matrix.csv

monte_carlo_results.csv

var_results.csv

Step 10: Build Individual Sheets
📈 1. Stock Price Trend
Chart: Line chart
Shows: Long-term stock growth
Business Meaning: Identify performance trends

📉 2. Daily Log Returns
Chart: Line chart
Shows: Market fluctuations
Business Meaning: Daily risk movement

📊 3. 30-Day Rolling Volatility
Chart: Line chart
Shows: Risk variation over time
Business Meaning: Detect unstable periods

🔥 4. Correlation Heatmap
Chart: Heatmap
Shows: Relationship between stocks
Business Meaning: Portfolio diversification

🎯 5. Monte Carlo Distribution (Histogram)
Chart: Histogram
Shows: Distribution of 10,000 future portfolio outcomes
Business Meaning: Probability-based risk modeling

Added:

VaR 95% vertical line

VaR 99% vertical line

Expected value (mean) line

🔹 PHASE 8 — DASHBOARD BUILDING
Step 11: Dashboard Design
Layout Flow:
Section	Purpose
Stock Trend + Returns	Performance
Volatility + Correlation	Risk
Monte Carlo Distribution	Future uncertainty
Step 12: Dashboard Storytelling
Logical Flow:

How stocks performed → How risky they are → How they correlate → What future risk looks like

This makes your dashboard executive-ready.

🔹 PHASE 9 — BUSINESS INTERPRETATION
Key Insights:
Portfolio is moderately diversified

Volatility spikes during market uncertainty

Monte Carlo shows majority outcomes between ₹900k – ₹1.3M

VaR 95% gives conservative loss estimate

VaR 99% shows extreme downside protection


