# RE 3.
import re


def is_valid_password(password: str) -> bool:
    if len(password) < 4:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    return True


if __name__ == "__main__":
    password = input("Введите пароль: ")
    print("Пароль валидный." if is_valid_password(password) else "Пароль не валидный.")
