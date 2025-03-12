# 9. Enum
from enum import Enum

class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"

class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):

        if isinstance(new_status, OrderStatus):
            self.status = new_status
        else:
            print("Неверный статус!")

    def display_status(self):
        print(f"Статус заказа {self.order_id}: {self.status.value}")


order1 = Order(order_id=1)
order1.display_status()

order1.update_status(OrderStatus.IN_PROGRESS)
order1.display_status()

order1.update_status(OrderStatus.READY)
order1.display_status()

# 10. Datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

date_str1 = input("Введите первую дату (в формате ГГГГ-ММ-ДД): ")
date_str2 = input("Введите вторую дату (в формате ГГГГ-ММ-ДД): ")

date1 = parser.parse(date_str1)
date2 = parser.parse(date_str2)

delta = abs(date2 - date1)

print(f"Количество дней между датами: {delta.days}")

#11. Datetime
from datetime import datetime

input_date = input("Введите дату (в формате ГГГГ-ММ-ДД): ")

try:
    parsed_date = datetime.strptime(input_date, "%Y-%m-%d")

    today = datetime.now()

    if parsed_date > today:
        print("Эта дата в будущем.")
    elif parsed_date < today:
        print("Эта дата в прошлом.")
    else:
        print("Введенная дата — это сегодня.")

except ValueError:
    print("Вы ввели неверный формат даты. Используйте формат ГГГГ-ММ-ДД.")

# 12. Logger
import logging

logging.basicConfig(
    filename='user_actions.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def log_action(message, level='INFO'):
    if level == 'INFO':
        logging.info(message)
    elif level == 'ERROR':
        logging.error(message)


def user_actions():
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить товар в корзину")
        print("2 - Оформить заказ")
        print("3 - Выйти из программы")

        action = input("Ваш выбор: ")

        if action == "1":
            product = input("Введите название товара для добавления в корзину: ")
            log_action(f"Пользователь добавил товар '{product}' в корзину.")
            print(f"Товар '{product}' добавлен в корзину.")
        elif action == "2":
            log_action("Пользователь оформил заказ.")
            print("Заказ успешно оформлен.")
        elif action == "3":
            log_action("Пользователь завершил работу с программой.")
            print("Выход из программы...")
            break
        else:
            log_action("Пользователь ввел неверную команду.", level='ERROR')
            print("Ошибка: Неверная команда.")


if __name__ == "__main__":
    user_actions()

# 13. Logger
import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)


handler = TimedRotatingFileHandler(
    'my_log.log',
    when='midnight',
    interval=1,
    backupCount=7,
    encoding='utf-8'
)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


logger.addHandler(handler)


logger.info('This is a log message')

# 14. Logger
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_format = '%(asctime)s - %(levelname)s - %(message)s'

file_handler = logging.FileHandler('user_actions.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_format))

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_action(message, level='INFO'):
    if level == 'INFO':
        logger.info(message)
    elif level == 'ERROR':
        logger.error(message)

def user_actions():
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить товар в корзину")
        print("2 - Оформить заказ")
        print("3 - Выйти из программы")

        action = input("Ваш выбор: ")

        if action == "1":
            product = input("Введите название товара для добавления в корзину: ")
            log_action(f"Пользователь добавил товар '{product}' в корзину.")
            print(f"Товар '{product}' добавлен в корзину.")
        elif action == "2":
            log_action("Пользователь оформил заказ.")
            print("Заказ успешно оформлен.")
        elif action == "3":
            log_action("Пользователь завершил работу с программой.")
            print("Выход из программы...")
            break
        else:
            log_action("Пользователь ввел неверную команду.", level='ERROR')
            print("Ошибка: Неверная команда.")

if __name__ == "__main__":
    user_actions()
