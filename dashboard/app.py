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

        # ✅ Correct file path usage
        df = pd.read_csv(file_path)

        # ✅ Clean column names
        df.columns = df.columns.str.strip().str.lower()

        # ✅ DEBUG (run once, then you can remove)
        print("Columns:", df.columns)

        # ✅ Handle missing columns safely
        if "quantity" not in df.columns:
            st.error("❌ 'quantity' column not found in dataset")
            st.stop()

        if "price" not in df.columns:
            st.error("❌ 'price' column not found in dataset")
            st.stop()

        # ✅ Create revenue column
        df["revenue"] = df["quantity"] * df["price"]

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
