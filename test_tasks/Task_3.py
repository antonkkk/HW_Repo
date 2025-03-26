# 3.
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Сумма чисел от 1 до {n} равна {total}")


number = int(input("Введите число: "))
sum_n(number)
