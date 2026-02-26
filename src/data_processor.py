import os
import pandas as pd

data_path = os.path.join(os.path.dirname(__file__), "..", "data", "orders.csv")

def load_data():
    return pd.read_csv(data_path)

def clean_data(df):
    df["revenue"] = df["quantity"] * df["price"]
    return df

if __name__ == "__main__":
    df = clean_data(load_data())
    print(df.tail())