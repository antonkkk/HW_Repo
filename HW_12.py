# 1.
class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Client with such ID already registered")
        self.clients[client_id] = name
        self.deposits[client_id] = None

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            raise ValueError("Client not registered")
        if self.deposits[client_id] is not None:
            raise ValueError("Client already has opened deposit")
        self.deposits[client_id] = {
            'start_balance': start_balance,
            'years': years,
            'current_balance': start_balance
        }

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.deposits or self.deposits[client_id] is None:
            raise ValueError("Deposit for current client not found")

        deposit = self.deposits[client_id]
        start_balance = deposit['start_balance']
        years = deposit['years']
        monthly_rate = 0.10 / 12
        months = years * 12

        final_balance = start_balance * (1 + monthly_rate) ** months
        return round(final_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits or self.deposits[client_id] is None:
            raise ValueError("Deposit for current client not found")

        final_balance = self.calc_deposit_interest_rate(client_id)
        self.deposits[client_id] = None
        return final_balance


# Example
client_id_outer = "0000001"

bank = Bank()
bank.register_client(client_id=client_id_outer, name="Siarhei")
bank.open_deposit_account(client_id=client_id_outer, start_balance=1000, years=1)

# Checking the calculation of the final amount
assert bank.calc_deposit_interest_rate(client_id=client_id_outer) == 1104.71, \
    "Error in calculating the total deposit amount"

# Closing a deposit
final_amount = bank.close_deposit(client_id=client_id_outer)
print(f"Final deposit sum: {final_amount}")


# 2.
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


# Example
book = Book(book_name="The Hobbit", author="J.R.R. Tolkien", num_pages=400, isbn="0006754023")

vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book)
petya.reserve_book(book)  # User can not reserve a book
vasya.cancel_reserve(book)

petya.reserve_book(book)
vasya.get_book(book)  # User can not get a book
petya.get_book(book)
vasya.return_book(book)  # User can not return a book
petya.return_book(book)

vasya.get_book(book)
