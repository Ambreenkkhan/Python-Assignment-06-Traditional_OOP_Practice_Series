# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.  

class Bank:
  # Class variable shared by all instances
  bank_name = "Meezan Bank"

  # Class method to change the class variable 'bank_name'
  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name  # Change the class variable using the cls keyword

  # Instance method to display the current bank name
  def display_bank_name(self):
    print(f"Bank Name: {Bank.bank_name}")  # Access class variable

# Create two instances (objects) of the Bank class
customer1 = Bank()
customer2 = Bank()

# Display the original bank name for both customers
customer1.display_bank_name()  
customer2.display_bank_name()  

# Change the bank name using the class method
Bank.change_bank_name("Bank AlHabib")

# Display the updated bank name
customer1.display_bank_name() 
customer2.display_bank_name() 
