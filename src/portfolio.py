import numpy as np
import pandas as pd

def portfolio_returns(
    returns: pd.DataFrame,
    weights: np.ndarray
) -> pd.Series:
    """
    Compute portfolio returns given asset returns and weights.

    Parameters
    ----------
    returns : pd.DataFrame
        Asset returns (rows: dates, columns: assets)
    weights : np.ndarray
        Portfolio weights

    Returns
    -------
    pd.Series
        Portfolio return time series
    """
    return pd.Series(
        returns.values @ weights,
        index=returns.index,
        name="Portfolio Return"
    )
