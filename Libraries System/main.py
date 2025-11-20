class Library:
    def __init__(self):
        self.books = ["Bhagavad Gita", "Ramayana", "Mahabharata", "Rigveda", "Shiva Purana"]

    def print_books(self):
        print("\n List of Books in the Library:")
        for book in self.books:
            print(f"- {book}")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' has been added to the library.")

    def show_number_of_books(self):
        print(f"\nTotal number of books in the library: {len(self.books)}")


# Create library object
l = Library()

# Interaction starts here
Que = input("Let's Explore the Library (say Yes or No):\n").lower()

if Que == 'yes':
    print('''\nWhat do you want to do?
    1. Visit the books
    2. Add a book to the Library
    3. Know the number of books in the Library''')

    choice = input(" Enter your choice (1, 2 or 3):\n")

    if choice == '1':
        l.print_books()

    elif choice == '2':
        book = input("Enter the name of the book you want to add:\n")
        l.add_book(book)

    elif choice == '3':
        l.show_number_of_books()

    else:
        print("Invalid choice.")

else:
    print("Ok! Thank you for visiting the Library.")
