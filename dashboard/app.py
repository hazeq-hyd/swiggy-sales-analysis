import os
import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Swiggy Sales Dashboard", layout="wide")

# File path
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "orders.csv")

st.title("🍔 Real-Time Swiggy Sales Dashboard")

placeholder = st.empty()

while True:
    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        # ✅ Clean column names
        df.columns = df.columns.str.strip().str.lower()

        # ✅ Show columns in UI (so we can debug easily)
        st.write("Columns in dataset:", list(df.columns))

        # ✅ Auto-detect important columns
        quantity_col = None
        price_col = None
        item_col = None
        city_col = None
        restaurant_col = None
        rating_col = None

        for col in df.columns:
            if "quant" in col or "qty" in col:
                quantity_col = col
            if "price" in col or "amount" in col:
                price_col = col
            if "item" in col or "product" in col:
                item_col = col
            if "city" in col:
                city_col = col
            if "restaurant" in col or "rest" in col:
                restaurant_col = col
            if "rating" in col:
                rating_col = col

        # ✅ If quantity missing → assume 1
        if quantity_col is None:
            df["quantity"] = 1
            quantity_col = "quantity"

        # ❌ If price missing → stop safely
        if price_col is None:
            st.error("❌ No price/amount column found in dataset")
            st.stop()

        # ✅ Revenue calculation
        df["revenue"] = df[quantity_col] * df[price_col]

        with placeholder.container():

            st.metric("💰 Total Revenue", f"₹ {df['revenue'].sum():,.0f}")

            # Top items
            if item_col:
                st.subheader("📦 Top Selling Items")
                st.bar_chart(df.groupby(item_col)[quantity_col].sum())

            # Revenue by city
            if city_col:
                st.subheader("🌆 Revenue by City")
                st.bar_chart(df.groupby(city_col)["revenue"].sum())

            # Ratings
            if restaurant_col and rating_col:
                st.subheader("⭐ Avg Rating by Restaurant")
                st.bar_chart(df.groupby(restaurant_col)[rating_col].mean())

    else:
        st.warning("⚠️ orders.csv file not found in data folder")

    time.sleep(5)
    st.rerun()
