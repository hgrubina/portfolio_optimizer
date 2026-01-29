import numpy as np
import pandas as pd
from scipy.stats import norm


def historical_var(
    returns: pd.Series,
    alpha: float = 0.05
):
    """
    Historical Value at Risk (VaR).

    Parameters
    ----------
    returns : pd.Series
        Portfolio returns.
    alpha : float
        Confidence level (e.g. 0.05 for 95% VaR).

    Returns
    -------
    float
        VaR value.
    """
    return np.percentile(returns, 100 * alpha)


def historical_cvar(
    returns: pd.Series,
    alpha: float = 0.05
):
    """
    Historical Conditional Value at Risk (CVaR).

    Parameters
    ----------
    returns : pd.Series
        Portfolio returns.
    alpha : float
        Confidence level.

    Returns
    -------
    float
        CVaR value.
    """
    var = historical_var(returns, alpha)
    return returns[returns <= var].mean()


def parametric_var(
    returns: pd.Series,
    alpha: float = 0.05
):
    """
    Parametric (Gaussian) Value at Risk.

    Parameters
    ----------
    returns : pd.Series
        Portfolio returns.
    alpha : float
        Confidence level.

    Returns
    -------
    float
        VaR value.
    """
    mu = returns.mean()
    sigma = returns.std()
    return norm.ppf(alpha, mu, sigma)


def parametric_cvar(
    returns: pd.Series,
    alpha: float = 0.05
):
    """
    Parametric (Gaussian) Conditional Value at Risk.

    Parameters
    ----------
    returns : pd.Series
        Portfolio returns.
    alpha : float
        Confidence level.

    Returns
    -------
    float
        CVaR value.
    """
    mu = returns.mean()
    sigma = returns.std()
    z = norm.ppf(alpha)
    return mu - sigma * norm.pdf(z) / alpha
