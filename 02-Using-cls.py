# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
class Counter:
    object_count = 0  # Class variable to track number of objects

    def __init__(self):
        # Increment count each time an object is created
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        # Display the number of objects created
        print(f"Total objects created: {cls.object_count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()


# Display object count using class method
Counter.display_count()
