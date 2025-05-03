# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A: # Base class A
    def show(self):
        print("Show method from class A")

class B(A):  # Class B inherits from A and overrides show()
    def show(self):
        print("Show method from class B")

class C(A): # Class C also inherits from A and overrides show()
    def show(self):
        print("Show method from class C")

# Class D inherits from both B and C (Diamond Inheritance)
class D(B, C):
    pass  # No override; uses method resolution order (MRO)

# Create an object of class D
d = D()

# Call the show() method — Python follows MRO to decide which method to use
d.show()

# Print the MRO of class D
print("Method Resolution Order:", D.__mro__)
