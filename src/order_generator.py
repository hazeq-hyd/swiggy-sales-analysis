import os
from faker import Faker
import random
import csv
import time
from datetime import datetime

print("Generator started...", flush=True)

fake = Faker()

restaurants = ["Dominos", "KFC", "Biryani House", "Pizza Hut", "Burger King"]
items = ["Burger", "Pizza", "Biryani", "Fries", "Sandwich"]
cities = ["Hyderabad", "Bangalore", "Chennai", "Mumbai", "Delhi"]

# Safe file path
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "orders.csv")

# Write header if file doesn't exist
file_exists = os.path.isfile(file_path)

def generate_order():
    return [
        datetime.now(),
        random.choice(restaurants),
        random.choice(items),
        random.randint(1, 5),
        random.randint(100, 500),
        random.choice(cities),
        random.randint(1, 5)
    ]

with open(file_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["timestamp","restaurant","item","quantity","price","city","rating"])

    while True:
        order = generate_order()
        writer.writerow(order)
        f.flush()
        print("New order added:", order, flush=True)
        time.sleep(2)