# RE 3.
def is_valid_password(password: str) -> bool:
    return (
        len(password) >= 4 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password)
    )

if __name__ == "__main__":
    password = input("Введите пароль: ")
    print("Пароль валидный." if is_valid_password(password) else "Пароль не валидный.")
