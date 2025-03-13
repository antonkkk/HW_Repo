# 10. Datetime
from dateutil import parser

date_str1 = input("Введите первую дату (в формате ГГГГ-ММ-ДД): ")
date_str2 = input("Введите вторую дату (в формате ГГГГ-ММ-ДД): ")

date1 = parser.parse(date_str1)
date2 = parser.parse(date_str2)

delta = abs(date2 - date1)

print(f"Количество дней между датами: {delta.days}")
