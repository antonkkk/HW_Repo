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
