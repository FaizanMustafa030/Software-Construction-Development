
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    
    def add_item(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(product)
        print(name, "added to the cart.")

   
    def calculate_total(self):
        total = 0

        for product in self.items:
            total = total + product["price"] * product["quantity"]

        return total

    
    def display_cart(self):
        print("\nCustomer:", self.customer_name)
       

        for product in self.items:
            print("Product:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

        print("Total Price:", self.calculate_total())



cart1 = ShoppingCart("Faizan")
cart2 = ShoppingCart("Mustafa")


cart1.add_item("Keyboard", 2500, 1)
cart1.add_item("Mouse", 1200, 2)

cart2.add_item("Headphones", 3500, 1)
cart2.add_item("USB Drive", 800, 3)

cart1.display_cart()
cart2.display_cart()
