class LibraryBook:
    def __init__(self, title, author, isbn, total_copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrowed_by = []

    def borrow_book(self, member_id):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.borrowed_by.append(member_id)
            return True
        return False

    def return_book(self, member_id):
        if member_id in self.borrowed_by:
            self.available_copies += 1
            self.borrowed_by.remove(member_id)
            return True
        return False

    def get_book_info(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'available': self.available_copies,
            'total': self.total_copies
        }

    def is_available(self):
        return self.available_copies > 0


def create_library():
    # Create a dictionary to store books with their titles as keys
    library = {}

    # Create some sample books
    books = [
        LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 2),
        LibraryBook("To Kill a Mockingbird", "Harper Lee", "978-0446310789", 3),
        LibraryBook("1984", "George Orwell", "978-0451524935", 1)
    ]

    # Add books to library dictionary
    for book in books:
        library[book.title] = book

    return library


lib = create_library()


def show_lib(library):
    for book in library.values():
        print(book.title)


show_lib(lib)
