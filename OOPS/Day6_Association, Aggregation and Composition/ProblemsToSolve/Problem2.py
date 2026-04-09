# 2: Library System (Aggregation)
# Design Book and Library classes to demonstrate aggregation.

# Features to be added to Book class
# Add below attributes:
# title
# author
# Add below methods:
# display_book() : Prints book details
# Features to be added to Library class
# Add below attributes:
# name
# books (list of Book objects)
# Add below methods:
# display_books() : Iterates and prints all book details
# Additional Requirements
# Create multiple Book objects outside the Library
# Pass them into Library
# Show that Book objects exist independently


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_book(self):
        print(f"Book Title: {self.title}, Author: {self.author}")
    
class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def display_books(self):
        print(f"Library: {self.name}")
        for book in self.books:
            book.display_book()
# Create Book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Create Library object
library = Library("Central Library", [book1, book2, book3])

# Display books in the library
library.display_books()
# Show that Book objects exist independently
print("\nBooks exist independently of the Library:")
book1.display_book()
book2.display_book()
book3.display_book()

