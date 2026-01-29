import sys
from pathlib import Path

# -------------------------------------------------
# Fix import path so Streamlit finds src/
# -------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

# -------------------------------------------------
# Standard imports
# -------------------------------------------------
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# -------------------------------------------------
# Project imports
# -------------------------------------------------
from src.data_loader import load_data, calculate_returns
from src.rebalancing import rebalance_portfolio
from src.risk_metrics import historical_var, historical_cvar
from src.stress_testing import historical_stress
from src.kpi import compute_kpis

# -------------------------------------------------
# Streamlit config
# -------------------------------------------------
st.set_page_config(
    page_title="Portfolio Optimizer Dashboard",
    layout="wide"
)

st.title("📈 Portfolio Optimization & Risk Dashboard")

# =================================================
# Sidebar — Configuration
# =================================================
st.sidebar.header("Configuration")

tickers = st.sidebar.multiselect(
    "Assets",
    options=["AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA"],
    default=["AAPL", "MSFT", "GOOG"]
)

start_date = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2020-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("2023-12-31")
)

rebalance_freq = st.sidebar.selectbox(
    "Rebalancing Frequency",
    options=["M", "Q", "Y"],
    index=0
)

if len(tickers) < 2:
    st.warning("Please select at least two assets.")
    st.stop()

# =================================================
# Data loading & calculations
# =================================================
prices = load_data(
    tickers,
    start_date.strftime("%Y-%m-%d"),
    end_date.strftime("%Y-%m-%d")
)

returns = calculate_returns(prices)

weights = np.ones(len(tickers)) / len(tickers)

portfolio_returns, weights_history = rebalance_portfolio(
    returns,
    weights,
    frequency=rebalance_freq
)

# =================================================
# Stress testing
# =================================================
stress_result = historical_stress(
    portfolio_returns,
    "2020-02-15",
    "2020-04-30"
)

# =================================================
# KPIs
# =================================================
kpis = compute_kpis(
    portfolio_returns=portfolio_returns,
    var_95=historical_var(portfolio_returns, 0.05),
    cvar_95=historical_cvar(portfolio_returns, 0.05),
    stress_result=stress_result
)

# =================================================
# KPI Dashboard
# =================================================
st.subheader("📊 Portfolio KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Annualized Return", f"{kpis['Return (Annualized)']:.2%}")
col2.metric("Annualized Volatility", f"{kpis['Volatility (Annualized)']:.2%}")
col3.metric("Sharpe Ratio", f"{kpis['Sharpe Ratio']:.2f}")
col4.metric("Max Drawdown", f"{kpis['Max Drawdown']:.2%}")

st.subheader("⚠️ Risk & Stress KPIs")

col5, col6, col7, col8 = st.columns(4)

col5.metric("VaR 95%", f"{kpis['VaR 95%']:.2%}")
col6.metric("CVaR 95%", f"{kpis['CVaR 95%']:.2%}")
col7.metric("Stress Return (COVID)", f"{kpis['Stress Period Return']:.2%}")
col8.metric("Stress Max Drawdown", f"{kpis['Stress Max Drawdown']:.2%}")

# =================================================
# Visualizations
# =================================================
st.subheader("📉 Portfolio Performance")

cum_returns = (1 + portfolio_returns).cumprod()

fig_perf = px.line(
    cum_returns,
    title="Cumulative Portfolio Performance"
)
st.plotly_chart(fig_perf, width="stretch")

# -------------------------------------------------
# Drawdown
# -------------------------------------------------
wealth = (1 + portfolio_returns).cumprod()
peak = wealth.cummax()
drawdown = (wealth - peak) / peak

fig_dd = px.area(
    drawdown,
    title="Portfolio Drawdown"
)
st.plotly_chart(fig_dd, width="stretch")

# -------------------------------------------------
# Asset allocation over time
# -------------------------------------------------
st.subheader("📊 Asset Allocation Over Time")

weights_df = weights_history.copy()
weights_df.index.name = "Date"
weights_long = weights_df.reset_index().melt(
    id_vars="Date",
    var_name="Asset",
    value_name="Weight"
)

fig_weights = px.area(
    weights_long,
    x="Date",
    y="Weight",
    color="Asset",
    title="Portfolio Weights Evolution"
)
st.plotly_chart(fig_weights, width="stretch")

# =================================================
# Stress Test Summary
# =================================================
st.subheader("🧨 Historical Stress Test (COVID Crash)")

st.write(
    f"""
    **Period:** {stress_result['start_date']} → {stress_result['end_date']}  
    **Cumulative Return:** {stress_result['cumulative_return']:.2%}  
    **Max Drawdown:** {stress_result['max_drawdown']:.2%}  
    **Volatility:** {stress_result['volatility']:.2%}
    """
)
