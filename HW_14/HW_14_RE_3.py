# RE 4.
import re


def fix_repeated_words(text):
    pattern = r'\b(\w+)\s+\1\b'
    corrected_text = re.sub(pattern, r'\1', text)
    return corrected_text


text = (
    "Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. "
    "Смешно, не не правда ли? Не нужно портить хор хоровод."
)

corrected_text = fix_repeated_words(text)
print(corrected_text)
