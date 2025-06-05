from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env na inicialização do módulo
load_dotenv()

# Interface abstrata para salvar dados
class DataStorage(ABC):
    @abstractmethod
    def save_current(self, data: dict):
        pass

    @abstractmethod
    def save_historical(self, df):
        pass


# Implementação para Supabase
from supabase import create_client

class SupabaseStorage(DataStorage):
    def __init__(self):
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        self.client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def save_current(self, data):
        if "error" in data:
            print("Error fetching current data:", data["error"])
            return
        response = self.client.table("stock_current").insert(data).execute()
        print("✅ Current data saved:", response)

    def save_historical(self, df):
        if "error" in df.columns:
            print("Error fetching historical data:", df.iloc[0]["error"])
            return
        records = df.to_dict(orient="records")
        response = self.client.table("stock_history").insert(records).execute()
        print("✅ Historical data saved:", response)


# Salvar em CSV
class CSVStorage(DataStorage):
    def __init__(self, current_file="current.csv", historical_file="history.csv"):
        self.current_file = current_file
        self.historical_file = historical_file

    def save_current(self, data):
        import csv
        if "error" in data:
            print("Error fetching current data:", data["error"])
            return
        with open(self.current_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:  # escreve header se arquivo vazio
                writer.writeheader()
            writer.writerow(data)
        print(f"✅ Current data saved to {self.current_file}")

    def save_historical(self, df):
        if "error" in df.columns:
            print("Error fetching historical data:", df.iloc[0]["error"])
            return
        df.to_csv(self.historical_file, mode='a', header=True, index=False)
        print(f"✅ Historical data saved to {self.historical_file}")