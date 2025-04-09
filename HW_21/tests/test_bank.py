import pytest
from loguru import logger


# Positive tests
def test_register_new_client(bank):
    logger.info("Регистрируем нового клиента")
    bank.register_client(1, "Иван Иванов")
    assert 1 in bank.clients
    assert bank.clients[1]['name'] == "Иван Иванов"


def test_open_deposit_for_client(bank):
    logger.info("Открываем депозит для клиента")
    bank.register_client(1, "Сидор Сидоров")
    bank.open_deposit_account(1, 50000, 3)
    assert 1 in bank.deposits
    assert bank.deposits[1]['balance'] == 50000
    assert bank.deposits[1]['years'] == 3


def test_calculate_deposit_interest(bank):
    logger.info("Проверяем расчет процентов")
    bank.register_client(1, "Петр Петров")
    bank.open_deposit_account(1, 100000, 2)
    amount = bank.calc_deposit_interest_rate(1)
    assert amount == round(100000 * (1 + 0.05/12)**(12*2), 2)


# Negative tests
def test_register_duplicate_client(bank):
    logger.info("Пробуем зарегистрировать существующего клиента")
    bank.register_client(1, "Ольга Ольговна")
    with pytest.raises(ValueError) as excinfo:
        bank.register_client(1, "Ольга Ольговна")
    assert "Client already exists" in str(excinfo.value)


def test_open_deposit_for_nonexistent_client(bank):
    logger.info("Пробуем открыть депозит без регистрации")
    with pytest.raises(ValueError) as excinfo:
        bank.open_deposit_account(999, 10000, 1)
    assert "Client not found" in str(excinfo.value)


def test_calculate_interest_for_nonexistent_deposit(bank):
    logger.info("Пробуем рассчитать проценты без депозита")
    bank.register_client(1, "Сергей Сергеев")
    with pytest.raises(ValueError) as excinfo:
        bank.calc_deposit_interest_rate(1)
    assert "Deposit not found" in str(excinfo.value)
