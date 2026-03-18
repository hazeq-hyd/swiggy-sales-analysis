import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "orders.csv")

df = pd.read_csv(file_path)

df = pd.read_csv("your_file.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

print(df.columns)  # debug

# Now safe to use
df["revenue"] = df["quantity"] * df["price"]
