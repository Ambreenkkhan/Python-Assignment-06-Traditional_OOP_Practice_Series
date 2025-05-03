# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
  @staticmethod   # Static method: does not depend on class or instance variables
  def celsius_to_fahrenheit(c):
    # Formula: (C × 9/5) + 32 = F
    return (c * 9/5) + 32

# Call the static method without creating an object
temp_c = 25  
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)  # Convert to Fahrenheit

print(f"{temp_c}°C is equal to {temp_f}°F")
