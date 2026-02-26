# Real-Time Swiggy Sales Analysis

This project simulates real-time food delivery orders and provides live sales insights.

## Features
- Real-time order simulation
- Revenue & sales insights
- SQLite database storage
- Live dashboard using Streamlit

## Run Project

### Install dependencies
pip install -r requirements.txt

### Start order generator
python src/order_generator.py

### Update database
python src/database.py

### Run dashboard
streamlit run dashboard/app.py