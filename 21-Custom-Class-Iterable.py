# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# Define a custom iterable class
class Countdown:
    # Constructor to initialize the starting number
    def __init__(self, start):
        self.start = start  # Store the initial value
        self.current = start  # Track the current value for iteration

    # __iter__ should return the iterator object (usually self)
    def __iter__(self):
        return self

    # __next__ returns the next value in the iteration
    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop iteration when reaching below 0
        value = self.current     # Store current value to return
        self.current -= 1        # Decrement for next call
        return value             # Return current countdown number

# Create an instance of Countdown with starting number 5
count = Countdown(5)

# Use a for-loop to iterate over the Countdown object
print("Countdown begins:")
for number in count:
    print(number)
