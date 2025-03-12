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
