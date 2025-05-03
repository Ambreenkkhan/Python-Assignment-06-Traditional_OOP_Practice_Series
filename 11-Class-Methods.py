# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
  # Class variable shared by all instances
  total_books = 0

  # Constructor to initialize book details
  def __init__(self, title, author):
    self.title = title     # Instance variable for book title
    self.author = author   # Instance variable for author name
    Book.increment_book_count()  # Call class method to update book count

  # Class method to update total_books
  @classmethod
  def increment_book_count(cls):
    cls.total_books += 1  # Increase class-level book count by 1

# Create multiple book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Print total number of books created
print("Total books:", Book.total_books) 
