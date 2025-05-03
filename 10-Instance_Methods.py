'''10. Instance Methods
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.'''

class Dog:
  
  # Constructor to initialize instance variables
  def __init__(self, name, breed):
    self.name = name      # (instance variable)
    self.breed = breed    # (instance variable)

  # Instance method: uses self to access instance data
  def bark(self):
    print(f"{self.name} is barking!") 

# Create an object (instance) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Call the instance method
dog1.bark()  

