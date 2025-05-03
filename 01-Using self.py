# ***06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Serie***
 
print("01-Using self: ")
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
class Student:
  # Constructor method to initialize name and marks of the student
  def __init__(self, name, marks):
    self.name = name       # Assign the provided name to the instance variable
    self.marks = marks     # Assign the provided marks to the instance variable

  # Method to display student's details
  def display(self):
    print(f"Student Name: {self.name}.   Marks:{self.marks}")  # Print the student's name and marks

# Create an instance of Student
student1: Student = Student("Aleena Khan", 93)

# Create another instance of Student
student2: Student = Student("Ali Khan", 91)

student1.display()

student2.display()
