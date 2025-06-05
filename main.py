from stock_fetcher import StockDataFetcher
from storage import SupabaseStorage, CSVStorage

if __name__ == "__main__":
    ticker = "PETR4.SA"
    fetcher = StockDataFetcher(ticker)

    current_data = fetcher.get_current_info()
    #print(current_data)
    #historical_data = fetcher.get_historical_data(days=10)
    #print(historical_data)

    # Seleção de qual banco de dados ou CSV
    # storage = SupabaseStorage()
    storage = CSVStorage()

    # Grava no banco de dados
    #storage.save_current(current_data)
    #storage.save_historical(historical_data)
