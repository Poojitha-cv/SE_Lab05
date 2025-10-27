
"""Inventory management system for adding, removing, and tracking items."""

import json
import ast
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to the stock_data dictionary."""
    if logs is None:
        logs = []

    # Validate inputs
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types for item or quantity.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specific quantity of an item from stock_data, if it exists."""
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types for item or quantity.")
        return

    if item not in stock_data:
        print(f"Item '{item}' not found in stock.")
        return

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]


def get_qty(item):
    """Return the quantity of the given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        stock_data.clear()
        stock_data.update(data)
    except FileNotFoundError:
        print("No existing inventory file found. Starting fresh.")


def save_data(file="inventory.json"):
    """Save current stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print all items and their quantities."""
    print("\nItems Report")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items that are below the given stock threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]


def safe_eval(expression):
    """Safely evaluate expressions using ast.literal_eval."""
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError):
        print("Unsafe or invalid expression.")
        return None


def main():
    """Main function for demonstrating inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("mango", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    safe_eval("'Eval safely replaced.'")


if __name__ == "__main__":
    main()
