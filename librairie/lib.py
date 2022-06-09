from ta.trend import  macd
from ta.momentum import rsi

def indic_tec(df):

    # Add Moving Average Convergence Divergence (MACD) indicator
    df["MACD"] = macd(close=df["Close"], window_slow=26, window_fast=12, fillna=True) # mazas

    # Add Relative Strength Index (RSI) indicator
    df["RSI"] = rsi(close=df["Close"], window=14, fillna=True)  # mazas

    return df