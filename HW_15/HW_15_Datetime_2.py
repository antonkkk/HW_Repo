# 11. Datetime
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
