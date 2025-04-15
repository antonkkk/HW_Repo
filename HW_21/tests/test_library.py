from loguru import logger


# Positive tests
def test_successful_book_reservation(book, reader):
    logger.info("Пробуем забронировать книгу")
    assert book.reserve(reader) is True
    assert book.reservation is not None
    assert book.reservation['reader'] == reader


def test_successful_book_borrowing(book, reader):
    logger.info("Пробуем получить книгу после брони")
    book.reserve(reader)
    assert book.get_book(reader) is True
    assert book.borrowed_by == reader
    assert book.reservation is None


def test_successful_book_return(book, reader):
    logger.info("Пробуем вернуть книгу")
    book.borrowed_by = reader
    assert book.return_book(reader) is True
    assert book.borrowed_by is None


# Negative tests
def test_reserve_already_borrowed_book(book, reader):
    logger.info("Пробуем забронировать взятую книгу")
    book.borrowed_by = reader
    assert book.reserve(reader) is False
    assert book.reservation is None


def test_return_not_borrowed_book(book, reader):
    logger.info("Пробуем вернуть не взятую книгу")
    assert book.return_book(reader) is False
