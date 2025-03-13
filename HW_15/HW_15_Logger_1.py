# 12. Logger
import logging

logging.basicConfig(
    filename='user_actions.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def user_actions():
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить товар в корзину")
        print("2 - Оформить заказ")
        print("3 - Выйти из программы")

        action = input("Ваш выбор: ")

        if action == "1":
            product = input("Введите название товара для добавления в корзину: ")
            logging.info(f"Пользователь добавил товар '{product}' в корзину.")
            print(f"Товар '{product}' добавлен в корзину.")
        elif action == "2":
            logging.info("Пользователь оформил заказ.")
            print("Заказ успешно оформлен.")
        elif action == "3":
            logging.info("Пользователь завершил работу с программой.")
            print("Выход из программы...")
            break
        else:
            logging.error("Пользователь ввел неверную команду.")
            print("Ошибка: Неверная команда.")


if __name__ == "__main__":
    user_actions()
