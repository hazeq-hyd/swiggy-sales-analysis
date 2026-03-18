import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "orders.csv")

# ✅ Read correct file
df = pd.read_csv(file_path)

# ✅ Clean column names (NO comma here)
df.columns = df.columns.str.strip().str.lower()

# ✅ Debug
print(df.columns)

# ✅ Safe revenue calculation (only if columns exist)
if "quantity" in df.columns and "price" in df.columns:
    df["revenue"] = df["quantity"] * df["price"]
else:
    print("❌ 'quantity' or 'price' column not found")
