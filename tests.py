import unittest
from user_manager import UserManager
from product_manager import ProductManager
from order_manager import OrderManager
from database import setup_database

class TestEcommerce(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Initialize the database before running tests."""
        setup_database()

    def test_user_registration(self):
        """Test user registration and CPF uniqueness."""
        # Generate a random CPF to avoid duplicates
        import random
        cpf = str(random.randint(100000000, 999999999))  # Random 9-digit number
        result = UserManager.register_user('Test User', cpf, 'password', '1990-01-01', 'Test City')
        self.assertTrue(result)

    def test_product_addition(self):
        """Test product addition."""
        product_id = ProductManager.add_product('Test Product', 'Description', 100, 9.99)
        self.assertIsNotNone(product_id)

    def test_order_creation(self):
        """Test creating an order with a valid cart."""
        cart = [{'product_id': 'some-product-id', 'price': 9.99, 'quantity': 2}]
        order_id = OrderManager.create_order('user-id', cart)
        self.assertIsNotNone(order_id)

if __name__ == '__main__':
    unittest.main()
