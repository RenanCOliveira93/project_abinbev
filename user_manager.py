import sqlite3
import hashlib
import uuid
from datetime import datetime

class UserManager:
    @staticmethod
    def register_user(name: str, cpf: str, password: str, birth_date: str, city: str) -> bool:
        """Register a new user with hashed password and unique CPF."""
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        user_id = str(uuid.uuid4())
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", 
                      (user_id, name, cpf, hashed_password, registration_date, birth_date, city))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Error during user registration: {e}")  # Add this to display errors
            return False
        finally:
            conn.close()

    @staticmethod
    def get_all_users() -> list:
        """Retrieve all users from the database."""
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        conn.close()
        return users
    
    @staticmethod
    def login(cpf: str, password: str) -> str:
        """
        Authenticate user with CPF and hashed password.

        :param cpf: The user's CPF for login.
        :param password: The plain-text password entered by the user.
        :return: The user's ID if authentication is successful, else None.
        """
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the entered password
        c.execute("SELECT id FROM users WHERE cpf = ? AND password = ?", (cpf, hashed_password))
        result = c.fetchone()
        conn.close()

        if result:
            return result[0]  # Return user ID if login is successful
        else:
            return None
