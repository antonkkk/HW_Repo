# 6.
def analyze_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()

        line_count = file_content.count('\n') + 1
        word_count = len(file_content.split())
        letter_count = len(file_content.replace(" ", "").replace("\n", ""))

        analysis_result = f"\n\nКоличество строк: {line_count}\nКоличество слов: {word_count}\nКоличество букв: {letter_count}"

        print(analysis_result)

        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(analysis_result)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")
    except Exception as error:
        print(f"Произошла ошибка: {error}")

file_name = "example.txt"
analyze_file(file_name)
