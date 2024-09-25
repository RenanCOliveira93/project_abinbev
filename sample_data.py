from datetime import datetime, timedelta
from user_manager import UserManager
from product_manager import ProductManager
import random

def generate_sample_data():
    """Generates sample data for users and products."""
    # Sample products
    products = [
        ("MacBook Pro", "High-performance laptop", 50, 1999.99),
        ("iPhone 13 Pro", "Apple's flagship phone", 100, 999.99),
        ("Sony WH-1000XM4", "Noise-canceling headphones", 70, 349.99)
    ]
    
    for product in products:
        ProductManager.add_product(*product)

    # Sample users
    cities = ["New York", "San Francisco", "Los Angeles"]
    for i in range(5):
        name = f"User{i+1}"
        cpf = f"{random.randint(10000000000, 99999999999)}"
        password = "password123"
        birth_date = (datetime.now() - timedelta(days=random.randint(5000, 10000))).strftime("%Y-%m-%d")
        city = random.choice(cities)
        UserManager.register_user(name, cpf, password, birth_date, city)
