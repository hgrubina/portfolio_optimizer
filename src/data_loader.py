import yfinance as yf
import pandas as pd


def load_data(tickers, start_date, end_date):
    """
    Descarga precios históricos desde Yahoo Finance de forma robusta.

    Soporta uno o múltiples tickers y distintos formatos de salida de yfinance.
    Prioriza 'Adj Close' si está disponible, caso contrario usa 'Close'.
    """

    raw = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=False
    )

    # Caso 1: columnas multinivel (múltiples tickers)
    if isinstance(raw.columns, pd.MultiIndex):
        if 'Adj Close' in raw.columns.levels[0]:
            prices = raw['Adj Close']
        else:
            prices = raw['Close']

    # Caso 2: columnas simples (un solo ticker)
    else:
        if 'Adj Close' in raw.columns:
            prices = raw[['Adj Close']].rename(columns={'Adj Close': tickers[0]})
        else:
            prices = raw[['Close']].rename(columns={'Close': tickers[0]})

    return prices.dropna()


def calculate_returns(prices):
    """
    Calcula retornos diarios simples.
    """
    return prices.pct_change().dropna()
