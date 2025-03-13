# 1.
def sequence_increasing(sequence):
    counter = 0
    for i in range(1, len(sequence)):
        if sequence[i - 1] >= sequence[i]:
            counter += 1
            if counter > 1:
                return False

            if i >= 2 and sequence[i - 2] >= sequence[i]:
                sequence[i] = sequence[i - 1]
    return True


print(sequence_increasing([1, 3, 2, 1]))


# 2.
def clock_value(n, f_number):
    return (f_number + n // 2) % 10


print(clock_value(10, 2))


# 3.
def card_number(number):
    number = str(number)
    if not number.isdigit():
        return False
    total_sum = 0
    reversed_num = number[::-1]
    for i in range(len(number)):
        digit = int(reversed_num[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit

    return total_sum % 10 == 0


print(card_number(4561261212345467))
