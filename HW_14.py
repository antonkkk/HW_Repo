# 1. Files
import os


def create_file(filename):

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Name,Group,Grades\n")
            file.write("John Smith,101,4 5 3 4\n")
            file.write("Peter Johnson,102,5 5 4 5\n")
            file.write("Michael Brown,101,3 4 4 3\n")
            file.write("David Wilson,103,5 4 5 4\n")


def read_file(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]
            students_count = len(lines)
            group_stats = {}

            for line in lines:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"Ошибка в строке: {line.strip()} (не хватает данных)")
                    continue

                name, group, grades = parts
                grades = list(map(int, grades.split()))

                if group not in group_stats:
                    group_stats[group] = {'count': 0, 'total_grades': 0, 'grades_count': 0}

                group_stats[group]['count'] += 1
                group_stats[group]['total_grades'] += sum(grades)
                group_stats[group]['grades_count'] += len(grades)


            group_averages = {group: round(stats['total_grades'] / stats['grades_count'], 2)
                              for group, stats in group_stats.items()}

            print(f"Общее количество студентов: {students_count}")
            print("Количество студентов в каждой группе:")
            for group, stats in group_stats.items():
                print(f"Группа {group}: {stats['count']} студентов")
            print("Средняя оценка по группам:")
            for group, avg in group_averages.items():
                print(f"Группа {group}: {avg}")

            return students_count, group_stats, group_averages
    except FileNotFoundError:
        print("Файл не найден!")
        return None, None, None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None, None


def append_statistics(filename, students_count, group_stats, group_averages):

    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"\nОбщее количество студентов: {students_count}\n")
            file.write("Количество студентов в каждой группе:\n")
            for group, stats in group_stats.items():
                file.write(f"Группа {group}: {stats['count']} студентов\n")
            file.write("Средняя оценка по группам:\n")
            for group, avg in group_averages.items():
                file.write(f"Группа {group}: {avg}\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


filename = "students.txt"
create_file(filename)
students_count, group_stats, group_averages = read_file(filename)
if students_count is not None:
    append_statistics(filename, students_count, group_stats, group_averages)

# 2.
import re


def find_dates_in_file(filename):

    date_pattern = re.compile(r'\b(\d{2}\.\d{2}\.\d{4})\b')

    with open(filename, 'r', encoding='utf-8') as file:

        for line in file:
            dates = date_pattern.findall(line)
            if dates:
                for date in dates:
                    print(date)


filename = 'textfile.txt'
find_dates_in_file(filename)

# 3.
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

# 4.
import re

def fix_repeated_words(text):
    pattern = r'\b(\w+)\s+\1\b'
    corrected_text = re.sub(pattern, r'\1', text)
    return corrected_text

text = "Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."

corrected_text = fix_repeated_words(text)
print(corrected_text)

# 6. XML
import xml.etree.ElementTree as ET
import os


def calculate_total_cost(xml_file):
    try:

        tree = ET.parse(xml_file)
        root = tree.getroot()

        total_cost = 0


        for product in root.findall('product'):

            price = float(product.find('price').text)
            quantity = int(product.find('quantity').text)


            total_cost += price * quantity

        return total_cost
    except FileNotFoundError:
        print(f"Ошибка: Файл '{xml_file}' не найден.")
        return None
    except ET.ParseError:
        print(f"Ошибка: Файл '{xml_file}' имеет неверный формат XML.")
        return None



if __name__ == "__main__":

    print("Текущая рабочая директория:", os.getcwd())


    xml_file = 'products.xml'

    total_cost = calculate_total_cost(xml_file)
    if total_cost is not None:
        print(f"Общая стоимость всех товаров: {total_cost}")

# 7. Json
import json


with open('clubs.json', 'r', encoding='utf-8') as file:
    clubs = json.load(file)


selected_countries = ["Франция", "Германия", "Италия"]
filtered_clubs = [club for club in clubs if club['страна'] in selected_countries]


max_wins_club = max(filtered_clubs, key=lambda club: club['победы'])


print(f"Клуб с наибольшим количеством побед:")
print(f"Название: {max_wins_club['название']}")
print(f"Страна: {max_wins_club['страна']}")
print(f"Количество побед: {max_wins_club['победы']}")

#8. YAML
import yaml


def load_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        return data['books']


def save_books(filename, books):
    with open(filename, 'w', encoding='utf-8') as file:
        yaml.dump({'books': books}, file, default_flow_style=False, allow_unicode=True)


def add_book(books):
    title = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    year = input("Введите год выпуска: ")

    new_book = {
        'title': title,
        'author': author,
        'year': int(year)
    }
    books.append(new_book)


def main():
    filename = 'books.yaml'

    books = load_books(filename)

    while True:
        print("\nТекущий список книг:")
        for book in books:
            print(f"{book['title']} - {book['author']} ({book['year']})")

        choice = input("\nХотите добавить книгу? (да/нет): ").strip().lower()
        if choice == 'да':
            add_book(books)
            save_books(filename, books)
            print("\nКнига добавлена!")
        else:
            break


if __name__ == "__main__":
    main()
