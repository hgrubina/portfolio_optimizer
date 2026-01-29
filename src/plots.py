# src/plots.py

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# -----------------------------
# Gráfico de Cumulative Returns
# -----------------------------
def plot_cumulative_returns(portfolio_returns: pd.Series) -> go.Figure:
    cumulative = (1 + portfolio_returns).cumprod()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=cumulative.index,
        y=cumulative.values,
        mode='lines',
        name='Cumulative Returns',
        line=dict(color='royalblue', width=3)
    ))
    fig.update_layout(
        title="Cumulative Portfolio Returns",
        xaxis_title="Date",
        yaxis_title="Cumulative Return",
        template="plotly_white"
    )
    return fig

# -----------------------------
# Gráfico de Drawdown
# -----------------------------
def plot_drawdown(portfolio_returns: pd.Series) -> go.Figure:
    cumulative = (1 + portfolio_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=drawdown.index,
        y=drawdown.values,
        mode='lines',
        name='Drawdown',
        line=dict(color='firebrick', width=3)
    ))
    fig.update_layout(
        title="Portfolio Drawdown",
        xaxis_title="Date",
        yaxis_title="Drawdown",
        template="plotly_white"
    )
    return fig

# -----------------------------
# Evolución de los pesos
# -----------------------------
def plot_weights_evolution(weights_history: pd.DataFrame, tickers: list) -> go.Figure:
    fig = go.Figure()
    for i, ticker in enumerate(tickers):
        fig.add_trace(go.Scatter(
            x=weights_history.index,
            y=weights_history[ticker],
            mode='lines',
            name=ticker,
            line=dict(width=3)
        ))
    fig.update_layout(
        title="Portfolio Weights Evolution",
        xaxis_title="Date",
        yaxis_title="Weight",
        template="plotly_white"
    )
    return fig

# -----------------------------
# Stress Test (ejemplo COVID)
# -----------------------------
def plot_stress_test(portfolio_returns: pd.Series, start: str, end: str) -> go.Figure:
    stress_returns = portfolio_returns[start:end]
    cumulative = (1 + stress_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=cumulative.index,
        y=cumulative.values,
        mode='lines',
        name='Cumulative Returns (Stress)',
        line=dict(color='darkorange', width=3)
    ))
    fig.add_trace(go.Scatter(
        x=drawdown.index,
        y=drawdown.values,
        mode='lines',
        name='Drawdown (Stress)',
        line=dict(color='crimson', width=3, dash='dot')
    ))
    fig.update_layout(
        title=f"Stress Test: {start} to {end}",
        xaxis_title="Date",
        yaxis_title="Value / Drawdown",
        template="plotly_white"
    )
    return fig

