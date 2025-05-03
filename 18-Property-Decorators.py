# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        # Private attribute to store the product price
        self._price = price

    # Getter method using @property decorator
    @property
    def price(self):
        print("Getting the price...")
        return self._price

    # Setter method to update the price
    @price.setter
    def price(self, new_price):
        print("Setting the price...")
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative!")

    # Deleter method to delete the price
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Create a Product object with an initial price
p = Product(100)

# Access the price using the getter
print("Price:", p.price)

# Update the price using the setter
p.price = 150
print("Updated Price:", p.price)

# Try setting a negative price
p.price = -50  # Should show a warning

# Delete the price using the deleter
del p.price
