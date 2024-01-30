# data.py

import random
import datetime

def get_latest_sales_data():
    # Placeholder function to simulate fetching the latest sales data
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales_data = {product: random.randint(10, 100) for product in products}
    return sales_data

def get_latest_inventory_data():
    # Placeholder function to simulate fetching the latest inventory data
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    inventory_data = {product: random.randint(50, 200) for product in products}
    return inventory_data

def get_latest_product_data():
    # Placeholder function to simulate fetching the latest product data
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    product_data = {product: random.randint(5, 50) for product in products}
    return product_data

def get_latest_sales_year_data():
    # Placeholder function to simulate fetching the latest yearly sales data
    years = [str(year) for year in range(2020, 2023)]
    sales_year_data = {year: random.randint(100, 1000) for year in years}
    return sales_year_data

def get_latest_inventory_month_data():
    # Placeholder function to simulate fetching the latest monthly inventory data
    now = datetime.datetime.now()
    months = [now - datetime.timedelta(days=i*30) for i in range(6, 0, -1)]  # Last 6 months
    months = [month.strftime('%b %Y') for month in months]
    inventory_month_data = {month: random.randint(200, 500) for month in months}
    return inventory_month_data
