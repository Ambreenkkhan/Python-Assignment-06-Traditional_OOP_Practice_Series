# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
  # This function runs when the object is created
  def __init__(self):
    print("Logger object has been created.")  # Show message when object is made

  # This function runs when the object is deleted
  def __del__(self):
    print("Logger object is being destroyed.")  # Show message when object is deleted

# Make an object of the Logger class
log: Logger = Logger()  # This runs the constructor and prints the message

# Delete the object
del log  # This runs the destructor and prints the message
