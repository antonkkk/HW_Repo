# 5.
def is_palindrome(input_value):
    input_str = str(input_value)
    return input_str == input_str[::-1]


user_input = input("Введите строку или число: ")

if is_palindrome(user_input):
    print(f" {user_input} - это палиндром")
else:
    print(f" {user_input} - это не палиндром")
