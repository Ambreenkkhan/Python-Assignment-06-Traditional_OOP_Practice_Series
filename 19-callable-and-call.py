# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    # Constructor to initialize the multiplier factor
    def __init__(self, factor):
        self.factor = factor  # Store the factor

    # Define __call__ method to make the object callable like a function
    def __call__(self, value):
        return value * self.factor  # Multiply the input value by the factor

# Create an instance of Multiplier with factor = 5
multiply_by_5 = Multiplier(5)

# Check if the object is callable
print("Is object callable?", callable(multiply_by_5))  # Output: True

# Call the object like a function with input value 10
result = multiply_by_5(10)  # Internally calls multiply_by_5.__call__(10)
print("Result of calling object:", result) 
