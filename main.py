from product_manager import ProductManager
from user_manager import UserManager
from order_manager import OrderManager
from sample_data import generate_sample_data
from database import setup_database

def main():
    setup_database()
    generate_sample_data()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. View All Users")
        print("4. View All Products")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            cpf = input("Enter CPF: ")
            password = input("Enter password: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            city = input("Enter city: ")
            if UserManager.register_user(name, cpf, password, birth_date, city):
                print("Registration successful!")
            else:
                print("Registration failed. CPF might already exist.")
        
        elif choice == '2':
            cpf = input("Enter CPF: ")
            password = input("Enter password: ")
            user_id = UserManager.login(cpf, password)
            if user_id:
                print("Login successful!")
                user_menu(user_id)
            else:
                print("Invalid credentials.")
                
        elif choice == '3':
            users = UserManager.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user[0]}, Name: {user[1]}, CPF: {user[2]}, Registration Date: {user[4]}, Birth Date: {user[5]}, City: {user[6]}")
            else:
                print("No users found.")
   #         for user in users:
    #            print(f"ID: {user[0]}, Name: {user[1]}, CPF: {user[2]}, City: {user[6]}")
                
        elif choice == '4':
            products = ProductManager.get_all_products()
            if products:
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Stock: {product[3]}, Price: ${product[4]:.2f}")
            else:
                print("No products found.")
            #for product in products:
             #   print(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[4]}")
                
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user_id):
    cart = []
    while True:
        print("\n1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. View Orders")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            products = ProductManager.get_all_products()
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[4]}")
        
        elif choice == '2':
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            product = ProductManager.get_product(product_id)
            if product and product[3] >= quantity:
                cart.append({'product_id': product_id, 'name': product[1], 'price': product[4], 'quantity': quantity})
                print("Added to cart!")
            else:
                print("Product unavailable or insufficient stock.")
        
        elif choice == '3':
            for item in cart:
                print(f"Product: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")
            print(f"Total: ${sum(item['price'] * item['quantity'] for item in cart)}")
        
        elif choice == '4':
            if cart:
                order_id = OrderManager.create_order(user_id, cart)
                print(f"Order placed successfully! Order ID: {order_id}")
                cart.clear()
            else:
                print("Cart is empty.")
        
        elif choice == '5':
            orders = OrderManager.get_user_orders(user_id)
            for order in orders:
                print(f"Order ID: {order[0]}, Date: {order[2]}, Total: ${order[3]}")
        
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
