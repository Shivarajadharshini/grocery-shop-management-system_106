# inventory.py
# Manage grocery products

class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary format: {product_name: [price, quantity]}

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        self.products[name] = [price, quantity]
        print(f"Product '{name}' added successfully!")

    def update_product(self):
        name = input("Enter product name to update: ")
        if name in self.products:
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            self.products[name] = [price, quantity]
            print(f"Product '{name}' updated successfully!")
        else:
            print(f"Product '{name}' does not exist.")

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        print("{:<20} {:<10} {:<10}".format("Product", "Price", "Quantity"))
        for name, (price, quantity) in self.products.items():
            print("{:<20} {:<10} {:<10}".format(name, price, quantity))
