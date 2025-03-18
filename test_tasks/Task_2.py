# 2.
def calculate_square():
    user_input = float(input("Введите число: "))
    value = user_input ** 2
    print(f"Квадрат числа {user_input} равен {value}")


def check_even_odd():
    user_number = int(input("Введите целое число: "))

    if user_number % 2 == 0:
        print(f"Число {user_number} является четным.")
    else:
        print(f"Число {user_number} является нечетным.")


calculate_square()
check_even_odd()
