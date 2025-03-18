# 7.
def build_string(input_str, count):
    if count < 1:
        return ""

    first_part = input_str[:count]
    second_part = first_part[:-1][::-1]
    return first_part + second_part


s = "abcdefghijklmnopqrstuvwxyz"
print(build_string(s, 1))  # "a"
print(build_string(s, 2))  # "aba"
print(build_string(s, 3))  # "abcba"
print(build_string(s, 4))  # "abcdcba"
print(build_string(s, 5))  # "abcdedcba"
