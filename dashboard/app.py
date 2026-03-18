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

        df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Show columns in UI
st.write("Columns in dataset:", df.columns)

# Auto-detect columns
quantity_col = None
price_col = None

for col in df.columns:
    if "quant" in col or "qty" in col:
        quantity_col = col
    if "price" in col or "amount" in col:
        price_col = col

# Stop if missing
if quantity_col is None:
    st.error(f"❌ Quantity column not found. Columns: {list(df.columns)}")
    st.stop()

if price_col is None:
    st.error(f"❌ Price column not found. Columns: {list(df.columns)}")
    st.stop()

# Create revenue safely
df["revenue"] = df[quantity_col] * df[price_col]

        with placeholder.container():
            st.metric("Total Revenue", f"₹ {df['revenue'].sum():,.0f}")

            if "item" in df.columns:
                st.subheader("Top Selling Items")
                st.bar_chart(df.groupby("item")["quantity"].sum())

            if "city" in df.columns:
                st.subheader("Revenue by City")
                st.bar_chart(df.groupby("city")["revenue"].sum())

            if "restaurant" in df.columns and "rating" in df.columns:
                st.subheader("Average Rating by Restaurant")
                st.bar_chart(df.groupby("restaurant")["rating"].mean())

    else:
        st.warning("⚠️ orders.csv file not found")

    time.sleep(5)
    st.rerun()
