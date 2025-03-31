# Custom Exceptions
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books (3).")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise BookNotFoundException(f"{book.title} is not borrowed by {self.name}.")

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = self._find_member(member_name)
        book = self._find_book(book_title)

        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")

        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self._find_member(member_name)
        book = self._find_book(book_title)

        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")

        member.return_book(book)

    def _find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def _find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def __str__(self):
        return f"Library:\nBooks: {[str(book) for book in self.books]}\nMembers: {[str(member) for member in self.members]}"


# Testing the Library Management System
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Add members
    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    print(library)

    # Borrow books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Bob", "The Great Gatsby")
        print(library)
    except Exception as e:
        print(e)

    # Try to borrow a non-existent book
    try:
        library.borrow_book("Alice", "Moby Dick")
    except Exception as e:
        print(e)

    # Try to borrow an already borrowed book
    try:
        library.borrow_book("Bob", "1984")
    except Exception as e:
        print(e)

    # Try to exceed the borrowing limit
    try:
        library.borrow_book("Alice", "The Great Gatsby")
    except Exception as e:
        print(e)

    # Return a book
    try:
        library.return_book("Alice", "1984")
        print(library)
    except Exception as e:
        print(e)

    # Try to return a book not borrowed by the member
    try:
        library.return_book("Bob", "1984")
    except Exception as e:
        print(e)
