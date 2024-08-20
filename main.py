import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data_csv"
    COLUMNS = ["date","amount","category","description"]

    @classmethod
    def initilize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category": category,
            "description": description
        }
        
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry is added")


CSV.initilize_csv()
CSV.add_entry("20-08-2024","200","Eatables","for Food")