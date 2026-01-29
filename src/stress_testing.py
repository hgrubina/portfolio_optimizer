import numpy as np
import pandas as pd


def historical_stress(
    portfolio_returns: pd.Series,
    start_date: str,
    end_date: str
):
    """
    Evaluates portfolio performance during a historical stress period.

    Parameters
    ----------
    portfolio_returns : pd.Series
        Portfolio returns indexed by date.
    start_date : str
        Stress period start (YYYY-MM-DD).
    end_date : str
        Stress period end (YYYY-MM-DD).

    Returns
    -------
    dict
        Stress performance metrics.
    """

    stressed = portfolio_returns.loc[start_date:end_date]

    cumulative_return = (1 + stressed).prod() - 1
    max_drawdown = _max_drawdown(stressed)

    return {
        "start_date": start_date,
        "end_date": end_date,
        "cumulative_return": cumulative_return,
        "max_drawdown": max_drawdown,
        "volatility": stressed.std() * np.sqrt(252)
    }


def rolling_worst_case(
    portfolio_returns: pd.Series,
    window: int = 252
):
    """
    Finds the worst rolling cumulative return.

    Parameters
    ----------
    portfolio_returns : pd.Series
        Portfolio returns.
    window : int
        Rolling window in days.

    Returns
    -------
    dict
        Worst rolling window metrics.
    """

    rolling_cum = (
        (1 + portfolio_returns)
        .rolling(window)
        .apply(lambda x: np.prod(x) - 1, raw=True)
    )

    worst_end = rolling_cum.idxmin()
    worst_start = worst_end - pd.Timedelta(days=window)

    stressed = portfolio_returns.loc[worst_start:worst_end]

    return {
        "start_date": worst_start,
        "end_date": worst_end,
        "cumulative_return": rolling_cum.min(),
        "max_drawdown": _max_drawdown(stressed)
    }


def synthetic_shock(
    portfolio_returns: pd.Series,
    shock_size: float = -0.20
):
    """
    Applies a one-day synthetic shock.

    Parameters
    ----------
    portfolio_returns : pd.Series
        Portfolio returns.
    shock_size : float
        Shock return (e.g. -0.20 = -20%).

    Returns
    -------
    pd.Series
        Returns including synthetic shock.
    """

    shocked = portfolio_returns.copy()
    shock_date = shocked.index[len(shocked) // 2]
    shocked.loc[shock_date] += shock_size

    return shocked


def _max_drawdown(returns: pd.Series):
    """
    Computes maximum drawdown.
    """
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()
