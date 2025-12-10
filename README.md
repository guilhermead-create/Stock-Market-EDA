# 📈 Brazilian Stock Analysis (B3)

## 📋 Project Overview
This project performs an **Exploratory Data Analysis (EDA)** on historical stock data from the Brazilian Stock Exchange (B3). The script collects data using the Yahoo Finance API, calculates key statistical indicators, and generates visualizations to identify trends and patterns over the last 12 months.

## 🚀 Features
* **Data Collection:** Automated download of historical data (Open, High, Low, Close, Volume) using `yfinance`.
* **Statistical Analysis:** Calculation of mean, median, standard deviation, and data integrity checks.
* **Technical Indicators:** Calculation of Simple Moving Averages (SMA-20) and Exponential Moving Averages (EMA-50).
* **Data Visualization:**
    * Price history (Line Chart).
    * Trading Volume (Bar Chart).
    * Correlation between Price and Volume (Scatter Plot).
    * Technical Analysis (Price vs. Moving Averages).

## 🛠️ Technologies Used
* **Python 3**
* **Pandas:** For data manipulation and analysis.
* **NumPy:** For numerical calculations.
* **Matplotlib:** For creating data visualizations.
* **yfinance:** API for retrieving financial data.

## 📊 How to Use
1.  Clone this repository.
2.  Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib yfinance
    ```
3.  Run the script (e.g., in Jupyter Notebook or VS Code).
4.  *Optional:* Change the `ticker` variable in the code to analyze a different stock (e.g., 'PETR4.SA', 'VALE3.SA', 'ITUB4.SA').

---
*Developed for educational purposes to demonstrate Python skills in Data Analysis.*
