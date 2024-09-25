import sqlite3
import uuid
from datetime import datetime

class OrderManager:
    @staticmethod
    def create_order(user_id: str, cart: list) -> str:
        """Create an order and update stock quantities for ordered items."""
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        order_id = str(uuid.uuid4())
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_amount = sum(item['price'] * item['quantity'] for item in cart)
        c.execute("INSERT INTO orders VALUES (?, ?, ?, ?)", (order_id, user_id, order_date, total_amount))

        for item in cart:
            c.execute("INSERT INTO order_items VALUES (?, ?, ?)", (order_id, item['product_id'], item['quantity']))
            c.execute("UPDATE products SET stock_quantity = stock_quantity - ? WHERE id = ?", 
                      (item['quantity'], item['product_id']))

        conn.commit()
        conn.close()
        return order_id

    @staticmethod
    def get_user_orders(user_id: str) -> list:
        """
        Retrieve all orders for a specific user.

        :param user_id: The ID of the user whose orders are to be retrieved.
        :return: A list of the user's orders.
        """
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = c.fetchall()
        conn.close()
        return orders