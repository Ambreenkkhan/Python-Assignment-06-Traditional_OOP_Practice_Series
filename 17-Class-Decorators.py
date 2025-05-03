# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    # Define a new method and add it to the class
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add the greet method to the class dynamically
    return cls         # Return the modified class

# Apply the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # Store person's name

# Create an instance of the Person class
p = Person("Ayaan")

# Call the greet() method added by the decorator
print(p.greet()) 
