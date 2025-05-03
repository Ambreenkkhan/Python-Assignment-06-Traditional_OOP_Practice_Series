'''9. Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().'''

# Import abc module to create abstract classes
from abc import ABC, abstractmethod

# Create an abstract class Shape
class Shape(ABC):
  
  # Define an abstract method area() - must be implemented in child class
  @abstractmethod
  def area(self):
    pass  # No implementation here

# Create a Rectangle class that inherits from Shape
class Rectangle(Shape):
  
  # Constructor to set width and height
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Implement the abstract method area()
  def area(self):
    return self.width * self.height  # Calculate and return area of rectangle

rect = Rectangle(5, 7)  # Create an object of Rectangle

print(f"Area of Rectangle: {rect.area()}")  # Print the area of the rectangle (5 * 3 = 15()) # Call the area method
