import pandas as pd
import yfinance as yf
import numpy as np

def download_price(symbol, start="2010-01-01", end=None):
    df = yf.download(symbol, start=start, end=end, progress=False)
    if df.empty:
        return df
    df = df[['Open','High','Low','Close','Adj Close','Volume']].copy()
    df.index = pd.to_datetime(df.index)
    df.reset_index(inplace=True)
    df.rename(columns={'Date':'date'}, inplace=True)
    df['trading_date'] = df['date'].dt.date
    return df

# Simple indicators (fallback if TA-Lib not installed)
def add_basic_indicators(df):
    df = df.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['ema_12'] = df['Adj Close'].ewm(span=12, adjust=False).mean()
    df['ema_26'] = df['Adj Close'].ewm(span=26, adjust=False).mean()
    df['macd'] = df['ema_12'] - df['ema_26']
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    df['ma_20'] = df['Adj Close'].rolling(20).mean()
    df['ma_50'] = df['Adj Close'].rolling(50).mean()
    # RSI
    delta = df['Adj Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    roll_up = up.ewm(com=13, adjust=False).mean()
    roll_down = down.ewm(com=13, adjust=False).mean()
    rs = roll_up / roll_down
    df['rsi_14'] = 100 - (100 / (1 + rs))
    return df


symbols = ['AAPL','MSFT','GOOGL']  # or top_stocks from news
for s in symbols:
    p = download_price(s, start='2010-01-01', end='2025-11-25')
    p = add_basic_indicators(p)
    p.to_csv(f"data/processed/prices_{s}.csv", index=False)
