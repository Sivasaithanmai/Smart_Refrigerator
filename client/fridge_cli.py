import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def list_items():
    resp = requests.get(f"{BASE_URL}/items/")
    items = resp.json()
    for item in items:
        print(f"{item['name']} | Qty: {item['quantity']} | Expires: {item['expiry_date']} | Category: {item['category']}")

def expiring_soon(days=3):
    resp = requests.get(f"{BASE_URL}/items/expiring-soon/?days={days}")
    items = resp.json()
    print(f"\nItems expiring in next {days} days:")
    for item in items:
        print(f"{item['name']} | Qty: {item['quantity']} | Expires: {item['expiry_date']}")

def grocery_suggestions():
    resp = requests.get(f"{BASE_URL}/items/grocery-suggestions/?min_quantity=1")
    items = resp.json()
    print("\nGrocery suggestions (low stock items):")
    for item in items:
        print(f"{item['name']} | Qty: {item['quantity']} | Category: {item['category']}")

def add_item():
    name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    expiry = input("Expiry Date (YYYY-MM-DD): ")
    category = input("Category: ")

    payload = {
        "name": name,
        "quantity": quantity,
        "expiry_date": expiry,
        "category": category
    }

    resp = requests.post(f"{BASE_URL}/items/", json=payload)
    if resp.status_code == 200:
        print("Item added successfully!")
    else:
        print("Failed to add item:", resp.text)

def main():
    while True:
        print("\n=== Smart Fridge CLI ===")
        print("1. List all items")
        print("2. Show expiring soon")
        print("3. Show grocery sugges
