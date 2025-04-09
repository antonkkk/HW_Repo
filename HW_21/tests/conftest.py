import pytest
from loguru import logger
import sys
from source.bank import Bank
from source.library import Book, Reader


def pytest_configure(config):
    logger.remove()
    logger.add(sys.stderr, level="INFO")


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def book():
    return Book("Clean Code", "Robert Martin", 464, "978-0132350884")


@pytest.fixture
def reader():
    return Reader("Test Reader")
