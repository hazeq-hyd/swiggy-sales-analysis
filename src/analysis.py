import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "orders.csv")

df = pd.read_csv(file_path)

df["revenue"] = df["quantity"] * df["price"]

print("\nTotal Revenue:")
print(df["revenue"].sum())

print("\nTop Selling Items:")
print(df.groupby("item")["quantity"].sum().sort_values(ascending=False))

print("\nRevenue by City:")
print(df.groupby("city")["revenue"].sum())

print("\nAverage Rating by Restaurant:")
print(df.groupby("restaurant")["rating"].mean())