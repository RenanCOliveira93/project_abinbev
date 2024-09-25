import sqlite3
import uuid

class ProductManager:
    @staticmethod
    def add_product(name: str, description: str, stock_quantity: int, price: float) -> str:
        """Add a product to the database."""
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        product_id = str(uuid.uuid4())
        c.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?)", (product_id, name, description, stock_quantity, price))
        conn.commit()
        conn.close()
        return product_id

    @staticmethod
    def get_all_products() -> list:
        """Retrieve all products from the database."""
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        products = c.fetchall()
        conn.close()
        return products

    @staticmethod
    def get_product(product_id: str) -> tuple:
        """Retrieve a product by its ID."""
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = c.fetchone()
        conn.close()
        return product
