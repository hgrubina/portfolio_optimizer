import numpy as np
import pandas as pd


def compute_kpis(
    portfolio_returns: pd.Series,
    var_95: float,
    cvar_95: float,
    stress_result: dict,
    risk_free_rate: float = 0.0,
    trading_days: int = 252
) -> dict:
    """
    Compute key portfolio KPIs.

    Parameters
    ----------
    portfolio_returns : pd.Series
        Daily portfolio returns.
    var_95 : float
        Historical Value at Risk at 95%.
    cvar_95 : float
        Historical Conditional VaR at 95%.
    stress_result : dict
        Output from historical_stress().
    risk_free_rate : float, optional
        Annual risk-free rate, default 0.
    trading_days : int, optional
        Number of trading days per year, default 252.

    Returns
    -------
    dict
        Dictionary with portfolio KPIs.
    """

    r = portfolio_returns.dropna()

    # --- Basic stats ---
    mean_daily = r.mean()
    vol_daily = r.std()

    mean_annual = mean_daily * trading_days
    vol_annual = vol_daily * np.sqrt(trading_days)

    sharpe = (
        (mean_annual - risk_free_rate) / vol_annual
        if vol_annual > 0 else np.nan
    )

    cumulative_return = (1 + r).prod() - 1

    # --- Drawdown ---
    wealth = (1 + r).cumprod()
    peak = wealth.cummax()
    drawdown = (wealth - peak) / peak
    max_drawdown = drawdown.min()

    # --- KPIs dictionary ---
    kpis = {
        "Return (Annualized)": mean_annual,
        "Volatility (Annualized)": vol_annual,
        "Sharpe Ratio": sharpe,
        "Cumulative Return": cumulative_return,
        "Max Drawdown": max_drawdown,
        "VaR 95%": var_95,
        "CVaR 95%": cvar_95,
        "Stress Period Return": stress_result["cumulative_return"],
        "Stress Max Drawdown": stress_result["max_drawdown"],
        "Stress Volatility": stress_result["volatility"],
    }

    return kpis
