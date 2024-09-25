import sqlite3

def setup_database() -> None:
    """Set up the database tables for the e-commerce backend."""
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()

    # Create Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT,
                cpf TEXT UNIQUE,
                password TEXT,
                registration_date TEXT,
                birth_date TEXT,
                city TEXT)''')

    # Create Products table
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                name TEXT,
                description TEXT,
                stock_quantity INTEGER,
                price REAL)''')

    # Create Orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                order_date TEXT,
                total_amount REAL,
                FOREIGN KEY(user_id) REFERENCES users(id))''')

    # Create OrderItems table
    c.execute('''CREATE TABLE IF NOT EXISTS order_items (
                order_id TEXT,
                product_id TEXT,
                quantity INTEGER,
                FOREIGN KEY(order_id) REFERENCES orders(id),
                FOREIGN KEY(product_id) REFERENCES products(id))''')

    conn.commit()
    conn.close()
