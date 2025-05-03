# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
  # Method to start the engine
  def start(self):
    print("Engine has started.")

# Define the Car class, which will use an Engine object
class Car:  # Define the Car class, which will use an Engine object

  def __init__(self, engine): # Constructor takes an Engine object as a parameter
    self.engine = engine  # Composition: Engine is part of Car

  # Method to start the car, which uses the Engine's start method
  def start_car(self):
    print("Starting the car...")
    self.engine.start()  # Accessing Engine's method through Car

# Create an Engine object
engine1 = Engine()

# Pass the Engine object to the Car class (composition)
car1 = Car(engine1)

# Use Car method, which internally uses Engine's method
car1.start_car()
