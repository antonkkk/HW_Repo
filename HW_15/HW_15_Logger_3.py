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


def user_actions():
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить товар в корзину")
        print("2 - Оформить заказ")
        print("3 - Выйти из программы")

        action = input("Ваш выбор: ")

        if action == "1":
            product = input("Введите название товара для добавления в корзину: ")
            logger.info(f"Пользователь добавил товар '{product}' в корзину.")
            print(f"Товар '{product}' добавлен в корзину.")
        elif action == "2":
            logger.info("Пользователь оформил заказ.")
            print("Заказ успешно оформлен.")
        elif action == "3":
            logger.info("Пользователь завершил работу с программой.")
            print("Выход из программы...")
            break
        else:
            logger.error("Пользователь ввел неверную команду.")
            print("Ошибка: Неверная команда.")


if __name__ == "__main__":
    user_actions()
