"""
Write a library class with no_of_books and books as two instance variables.
write a program to create a library form this library class and show how you can print all books,
add a book and get the number pf books using different methods.
show that your program does not persist the books after the program is stopped.

"""

class Library:
    """
    A class to represent a library.
    Attributes:
        no_of_books (int): Number of books in the library.
        books (list): List of book titles.
    """
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_books(self, book):
        """
        Add a book to the library.
        Args:
            book (str): The name of the book to add.
        """
        self.books.append(book)
        self.no_of_books = len(self.books)
        print(f"Book '{book}' has been added successfully!")

    def book_info(self):
        """
        Display all books in the library.
        """
        if self.no_of_books > 0:
            print(f"\nThere are {self.no_of_books} book(s) in the library:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")
        else:
            print("\nThe library is currently empty. Please add some books first.")

    def no_of_book(self):
        """
        Display the number of books in the library.
        """
        print(f"\nTotal number of books: {self.no_of_books}")

    def rename_book(self, book_name):
        """
        Rename a book in the library.
        Args:
            book_name (str): The name of the book to rename.
        """
        if self.no_of_books > 0:
            if book_name in self.books:
                index = self.books.index(book_name)
                correct_name = input("Enter the correct name of the book: ").strip()
                if correct_name:
                    self.books[index] = correct_name
                    print(f"Book '{book_name}' has been successfully renamed to '{correct_name}'.")
                else:
                    print("\nNew name cannot be empty!")
            else:
                print("\nInvalid book name. Please try again.")
        else:
            print("\nThe library is currently empty. Please add some books first.")

    def deleted_book(self, book_name):
        """
        Delete a book from the library.
        Args:
            book_name (str): The name of the book to delete.
        """
        if self.no_of_books > 0:
            if book_name in self.books:
                self.books.remove(book_name)
                self.no_of_books = len(self.books)
                print(f"Book '{book_name}' has been successfully deleted!")
            else:
                print("\nInvalid book name. Please try again.")
        else:
            print("\nThe library is currently empty. Please add some books first.")


# Main Program
if __name__ == "__main__":
    lib = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Show book information")
        print("3. Show total number of books")
        print("4. Delete a book")
        print("5. Rename a book")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): ").strip())
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            book_name = input("\nEnter the name of the book: ").strip()
            if book_name:
                lib.add_books(book_name)
            else:
                print("\nBook name cannot be empty!")
        elif choice == 2:
            lib.book_info()
        elif choice == 3:
            lib.no_of_book()
        elif choice == 4:
            book_name = input("Enter the name of the book to delete: ").strip()
            if book_name:
                lib.deleted_book(book_name)
            else:
                print("\nBook name cannot be empty!")
        elif choice == 5:
            book_name = input("Enter the name of the book to rename: ").strip()
            if book_name:
                lib.rename_book(book_name)
            else:
                print("\nBook name cannot be empty!")
        elif choice == 6:
            print("\nThank you for using the library system. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select an option between 1 and 6.")