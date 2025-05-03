# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the cl
class Car:
  # Public variable 'brand'
  def __init__(self, brand):
    self.brand = brand  # This is a public variable that stores the brand of the car

  # Public method 'start'
  def start(self):
    print(f"The {self.brand} car has started.")  # This is a public method accessible from outside

# Create an instance (object) 
my_car = Car("Toyota")

# Access the public variable 'brand' from outside the class
print("Car Brand:", my_car.brand)

# Call the public method 'start' from outside the class
my_car.start()
