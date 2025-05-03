# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.
class MathUtils:
  # Define a static method
  @staticmethod
  def add(a, b):
    return a + b  # Return the sum of a and b

# Call the static method directly from the class without creating an instance
result = MathUtils.add(10, 5)

print(f"The sum of 10 and 5 is:", result)
