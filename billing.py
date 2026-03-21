# billing.py
# Handle billing

class Billing:
    def __init__(self, inventory, tax_rate):
        self.inventory = inventory
        self.tax_rate = tax_rate

    def generate_bill(self):
        if not self.inventory.products:
            print("No products in inventory to bill.")
            return

        cart = {}
        while True:
            product_name = input("Enter product name (or 'done' to finish): ")
            if product_name.lower() == "done":
                break
            if product_name not in self.inventory.products:
                print("Product not found in inventory.")
                continue
            quantity = int(input("Enter quantity: "))
            price, stock = self.inventory.products[product_name]
            if quantity > stock:
                print(f"Not enough stock. Available: {stock}")
                continue
            cart[product_name] = quantity
            self.inventory.products[product_name][1] -= quantity

        if not cart:
            print("No items purchased.")
            return

        total = 0
        print("\n===== BILL =====")
        print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Price", "Quantity", "Amount"))
        for name, quantity in cart.items():
            price = self.inventory.products[name][0]
            amount = price * quantity
            total += amount
            print("{:<20} {:<10} {:<10} {:<10}".format(name, price, quantity, amount))

        tax = total * self.tax_rate / 100
        grand_total = total + tax
        print(f"\nSubtotal: {total:.2f}")
        print(f"Tax ({self.tax_rate}%): {tax:.2f}")
        print(f"Grand Total: {grand_total:.2f}")
