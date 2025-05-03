#  Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.



class Employee:
  def __init__(self, name, salary, ssn):
    self.name = name        # Public variable: can be accessed anywhere
    self._salary = salary   # Protected variable: can be accessed within the class
    self.__ssn = ssn        # Private variable: cannot be accessed directly outside the class

# Create an object of the Employee class
emp = Employee("Ali Adnan", 1000000, "123-45-6789") 
 
# Access public variable
print("Name:", emp.name)  # Works fine

# Access protected variable
print("Salary:", emp._salary)  # Works, but not recommended to access from outside the class

# Try to access private variable
# This will cause an error
print("SSN:", emp.__ssn)  

# Correct way to access private variable (if needed)
# print("SSN (accessed using name mangling):", emp._Employee__ssn)  # Works using name mangling
