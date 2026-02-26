import os
import sqlite3
from data_processor import load_data, clean_data

base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "..", "data", "orders.db")

conn = sqlite3.connect(db_path)

df = clean_data(load_data())
df.to_sql("orders", conn, if_exists="replace", index=False)

conn.close()

print("Database updated successfully")