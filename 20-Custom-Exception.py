# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Step 1: Define a custom exception class by inheriting from Exception
class InvalidAgeError(Exception):
    # Constructor with a custom message
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)  # Call the base class constructor

# Step 2: Define a function that checks age and raises the custom exception
def check_age(age):
    if age < 18:
        # Raise the custom exception if age is less than 18
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print("Age is valid. You are eligible.")  # Valid age message

# Step 3: Use try-except to handle the exception
try:
    user_age = int(input("Enter your age: "))  # Get user input
    check_age(user_age)                        # Call the function
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)       # Handle custom exception
except ValueError:
    print("Please enter a valid number.")      # Handle non-integer input
