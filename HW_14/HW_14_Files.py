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
