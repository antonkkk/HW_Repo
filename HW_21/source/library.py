class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reservation = None
        self.borrowed_by = None

    def reserve(self, reader):
        if self.reservation is not None or self.borrowed_by is not None:
            return False
        self.reservation = {'reader': reader, 'is_reserved': True}
        return True

    def cancel_reserve(self, reader):
        if self.reservation and self.reservation['reader'] == reader:
            self.reservation = None
            return True
        return False

    def get_book(self, reader):
        if self.borrowed_by is not None:
            return False
        if self.reservation and self.reservation['reader'] != reader:
            return False
        self.borrowed_by = reader
        self.reservation = None
        return True

    def return_book(self, reader):
        if self.borrowed_by == reader:
            self.borrowed_by = None
            return True
        return False


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book_obj):
        if book_obj.reserve(self):
            print(f"{self.name} successfully reserved the book '{book_obj.book_name}'.")
        else:
            print(f"{self.name} can't reserve the book '{book_obj.book_name}'.")

    def cancel_reserve(self, book_obj):
        if book_obj.cancel_reserve(self):
            print(f"{self.name} successfully canceled the reservation '{book_obj.book_name}'.")
        else:
            print(f"{self.name} can't cancel the reservation of the book '{book_obj.book_name}'.")

    def get_book(self, book_obj):
        if book_obj.get_book(self):
            print(f"{self.name} successfully borrowed the book '{book_obj.book_name}'.")
        else:
            print(f"{self.name} can't borrow the book '{book_obj.book_name}'.")

    def return_book(self, book_obj):
        if book_obj.return_book(self):
            print(f"{self.name} successfully returned the book '{book_obj.book_name}'.")
        else:
            print(f"{self.name} can't return the book '{book_obj.book_name}'.")
