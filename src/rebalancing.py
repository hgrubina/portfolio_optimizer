import numpy as np
import pandas as pd


def rebalance_portfolio(
    returns: pd.DataFrame,
    initial_weights: np.ndarray,
    frequency: str = "M"
):
    """
    Simulates portfolio evolution with periodic rebalancing.

    Parameters
    ----------
    returns : pd.DataFrame
        Asset returns (daily), indexed by date.
    initial_weights : np.ndarray
        Initial portfolio weights (sum to 1).
    frequency : str
        Rebalancing frequency:
        'M' = monthly
        'Q' = quarterly
        'A' = annual

    Returns
    -------
    portfolio_returns : pd.Series
        Portfolio returns over time.
    weights_history : pd.DataFrame
        Asset weights over time.
    """

    if not np.isclose(initial_weights.sum(), 1.0):
        raise ValueError("Initial weights must sum to 1.")

    assets = returns.columns
    dates = returns.index

    # Initialize
    weights = initial_weights.copy()
    weights_history = []
    portfolio_returns = []

    last_rebalance = dates[0]

    for date in dates:
        r = returns.loc[date].values

        # Portfolio return
        port_ret = np.dot(weights, r)
        portfolio_returns.append(port_ret)

        # Update weights due to drift
        weights = weights * (1 + r)
        weights = weights / weights.sum()

        # Save weights
        weights_history.append(weights.copy())

        # Check rebalance condition
        if date.to_period(frequency) != last_rebalance.to_period(frequency):
            weights = initial_weights.copy()
            last_rebalance = date

    portfolio_returns = pd.Series(
        portfolio_returns,
        index=dates,
        name="Portfolio Return"
    )

    weights_history = pd.DataFrame(
        weights_history,
        index=dates,
        columns=assets
    )

    return portfolio_returns, weights_history
