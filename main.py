import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE = "finance_data_csv"
    COLUMNS = ["date","amount","category","description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initilize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"],format=CSV.FORMAT)
        start_date = datetime.strptime(start_date,CSV.FORMAT)
        end_date = datetime.strptime(end_date,CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print('No transactions found given in the date range')
        else:
            print(f'here are transaction {start_date} and {end_date}')
            print(
                filtered_df.to_string(index=False, 
                            formatters = {"date": lambda x:x.strftime(CSV.FORMAT)})

            )

            total_income = filtered_df[filtered_df["category"]=="Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"]=="Expense"]["amount"].sum()
            print("\n Summary: ")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings : ${(total_income-total_expense):.2f}" )
        
        return filtered_df


    
    
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

def add():
    CSV.initilize_csv()
    date = get_date("Enter the transaction date", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)

CSV.get_transactions("19-08-2024","20-08-2024")
# add()



