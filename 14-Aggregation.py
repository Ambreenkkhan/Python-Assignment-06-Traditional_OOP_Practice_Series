# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
  # Constructor to initialize employee details
  def __init__(self, name, emp_id):
    self.name = name       
    self.emp_id = emp_id   

  # Method to display employee information
  def show_details(self):
    print(f"Employee Name: {self.name}, ID: {self.emp_id}")

# Define the Department class
class Department:
  # Constructor takes an independent Employee object
  def __init__(self, dept_name, employee):
    self.dept_name = dept_name      # Name of the department
    self.employee = employee        # Aggregated Employee object

  # Method to display department and employee info
  def show_department(self):
    print(f"Department: {self.dept_name}")
    self.employee.show_details()    # Access Employee's method

# Create an Employee object independently
emp1 = Employee("Ambreen Khan", 101)

# Create a Department object and pass the Employee object (Aggregation)
dept1 = Department("Human Resources", emp1)

# Show department and associated employee info
dept1.show_department()
