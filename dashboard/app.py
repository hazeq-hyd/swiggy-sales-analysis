import os
import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Swiggy Sales Dashboard", layout="wide")

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "orders.csv")

st.title("🍔 Real-Time Swiggy Sales Dashboard")

placeholder = st.empty()

while True:
    if os.path.exists(file_path):
        df = pd.read_csv("your_file.csv")

# Clean column names (handles ALL issues)
df.columns = df.columns.str.strip().str.lower()

print(df.columns)  # debug once

# Now this will work safely
df["revenue"] = df["quantity"] * df["price"]
        with placeholder.container():
            st.metric("Total Revenue", f"₹ {df['revenue'].sum():,.0f}")

            st.subheader("Top Selling Items")
            st.bar_chart(df.groupby("item")["quantity"].sum())

            st.subheader("Revenue by City")
            st.bar_chart(df.groupby("city")["revenue"].sum())

            st.subheader("Average Rating by Restaurant")
            st.bar_chart(df.groupby("restaurant")["rating"].mean())

    time.sleep(5)
    st.rerun()
