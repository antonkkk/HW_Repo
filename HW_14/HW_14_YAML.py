# 8. YAML
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
