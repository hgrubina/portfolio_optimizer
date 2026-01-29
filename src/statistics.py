import numpy as np
import pandas as pd


TRADING_DAYS = 252


def portfolio_return(returns: pd.DataFrame, weights: np.ndarray) -> float:
    """
    Retorno esperado anualizado del portafolio.
    """
    mean_daily = returns.mean().values
    return np.dot(weights, mean_daily) * TRADING_DAYS


def portfolio_volatility(returns: pd.DataFrame, weights: np.ndarray) -> float:
    """
    Volatilidad anualizada del portafolio.
    """
    cov = returns.cov().values * TRADING_DAYS
    return np.sqrt(weights.T @ cov @ weights)


def sharpe_ratio(
    returns: pd.DataFrame,
    weights: np.ndarray,
    risk_free_rate: float = 0.01
) -> float:
    """
    Sharpe Ratio anualizado.
    """
    ret = portfolio_return(returns, weights)
    vol = portfolio_volatility(returns, weights)
    return (ret - risk_free_rate) / vol


def sortino_ratio(
    returns: pd.DataFrame,
    weights: np.ndarray,
    risk_free_rate: float = 0.01
) -> float:
    """
    Sortino Ratio anualizado.
    """
    portfolio_returns = returns @ weights
    downside = portfolio_returns[portfolio_returns < 0]

    downside_vol = np.sqrt(
        (downside ** 2).mean()
    ) * np.sqrt(TRADING_DAYS)

    ret = portfolio_return(returns, weights)
    return (ret - risk_free_rate) / downside_vol


def portfolio_summary(
    returns: pd.DataFrame,
    weights: np.ndarray,
    risk_free_rate: float = 0.01
) -> dict:
    """
    Resumen completo de métricas del portafolio.
    """
    return {
        "return": portfolio_return(returns, weights),
        "volatility": portfolio_volatility(returns, weights),
        "sharpe": sharpe_ratio(returns, weights, risk_free_rate),
        "sortino": sortino_ratio(returns, weights, risk_free_rate),
    }
