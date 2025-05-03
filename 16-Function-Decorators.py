# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()
def log_function_call(func):
    # Wrapper function that adds extra behavior
    def wrapper():
        print("Function is being called")  # Log message before function call
        func()  # Call the original function
    return wrapper  # Return the wrapped version

# Define a function and apply the decorator using @ syntax
@log_function_call
def say_hello():
    print("Hello, world!")

say_hello()
