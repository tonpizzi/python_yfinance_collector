import yfinance as yf
import pandas as pd
from datetime import datetime

class StockDataFetcher:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)

    def get_current_info(self):
        try:
            info = self.ticker.info
            return {
                "symbol": self.ticker_symbol,
                "name": info.get("longName"),
                "price": info.get("regularMarketPrice"),
                "change_percent": info.get("regularMarketChangePercent"),
                "currency": info.get("currency"),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}

    def get_historical_data(self, days):
        try:
            df = self.ticker.history(period=f"{days}d")
            df.reset_index(inplace=True)
            df["symbol"] = self.ticker_symbol
            df.rename(columns={
                "Date": "date",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume"
            }, inplace=True)
            return df[["date", "symbol", "open", "high", "low", "close", "volume"]]
        except Exception as e:
            return pd.DataFrame([{"error": str(e)}])
