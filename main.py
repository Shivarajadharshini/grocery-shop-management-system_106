# main.py
# Grocery Shop Management System

from inventory import Inventory
from billing import Billing
from config import TAX_RATE

def main():
    inventory = Inventory()
    billing_system = Billing(inventory, TAX_RATE)

    while True:
        print("\n=== Grocery Shop Management System ===")
        print("1. Add Product")
        print("2. Update Product")
        print("3. View Inventory")
        print("4. Generate Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.add_product()
        elif choice == "2":
            inventory.update_product()
        elif choice == "3":
            inventory.view_inventory()
        elif choice == "4":
            billing_system.generate_bill()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
