
import random
import datetime

def get_latest_sales_data():
    
    products = ['PING', 'DNS', 'TELNET', 'VOICE', 'CSI','CSA','QUAKE3' ]
    sales_data = {product: random.randint(10, 100) for product in products}
    return sales_data

def get_latest_inventory_data():
    
    products = ['1', '2', '3', '4', '5']
    inventory_data = {product: random.randint(50, 200) for product in products}
    return inventory_data

def get_latest_product_data():
    
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    product_data = {product: random.randint(5, 50) for product in products}
    return product_data

def get_latest_sales_year_data():
    
    years = [str(year) for year in range(2020, 2023)]
    sales_year_data = {year: random.randint(100, 1000) for year in years}
    return sales_year_data

def get_latest_inventory_month_data():
   products = ['shared service', 'dedicated services', 'realtime', 'unknow services']
   inventory_month_data = {product: random.randint(0, 100) for product in products}
   return inventory_month_data
