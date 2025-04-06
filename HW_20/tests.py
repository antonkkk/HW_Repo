import unittest
from bank import Bank
from library import Book, Reader


class BankTests(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.client_id = "001"
        self.bank.register_client(self.client_id, "Test Client")

    def test_deposit_operations(self):
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        self.assertGreater(self.bank.calc_deposit_interest_rate(self.client_id), 1000)

    def test_nonexistent_client(self):
        with self.assertRaises(ValueError):
            self.bank.open_deposit_account("002", 1000, 1)


class BookTests(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Book", "Author", 100, "123")
        self.reader1 = Reader("Reader1")
        self.reader2 = Reader("Reader2")

    def test_reserve_success(self):
        self.assertTrue(self.book.reserve(self.reader1))

    def test_reserve_fail(self):
        self.book.reserve(self.reader1)
        self.assertFalse(self.book.reserve(self.reader2))

    def test_get_return_success(self):
        self.assertTrue(self.book.get_book(self.reader1))
        self.assertTrue(self.book.return_book(self.reader1))


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Book", "Author", 100, "123")
        self.reader = Reader("Test Reader")

    def test_operations(self):
        self.reader.reserve_book(self.book)
        self.reader.get_book(self.book)
        self.reader.return_book(self.book)


if __name__ == '__main__':
    unittest.main()