# 8. The super() Function
#    Assignment:
#    Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Create a base class called Person
class Person:
  def __init__(self, name):
    self.name = name  # Set the name attribute
    print(f"Person constructor called. Name: {self.name}")

# Create a derived class called Teacher that inherits from Person
class Teacher(Person):
  def __init__(self, name, subject):
    super().__init__(name)  # Call the constructor of the base class using super()
    self.subject = subject  # Set the subject attribute
    print(f"Teacher constructor called. Subject: {self.subject}")

# Create an object of the Teacher class
teacher1 = Teacher("Miss Aleena", "Mathematics")
