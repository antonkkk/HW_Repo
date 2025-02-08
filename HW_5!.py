#1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
import l

name = "www.my_site.com#about"
print(name.replace("#","/"))

#2. Напишите программу, которая добавляет ‘ing’ к словам
word = "word"
print(word + "ing")

#3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
names = "Ivanou Ivan"
words = names.split()
reversed_names = ' '.join(words[::-1])
print(reversed_names)

#4. Напишите программу, которая удаляет пробел в начале, в конце строки
text = " Hello World "
print(text.strip())

#5. Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
city = "pARiS"
new_city = city.capitalize()
print(new_city)

#6. Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
s1 = "Robin Singh"
l1 = s1.split()
print(l1)

#7. Перевести строку в список "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
s2 = "I love arrays they are my favorite"
l2 = s2.split()
print(l2)

#8. Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus. Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
l3 = ["Ivan", "Ivanou"]
l4 = ' '.join(l3)
s3 = "Minsk"
s4 = "Belarus"
print(f"Привет, {l4}! Добро пожаловать в {s3} {s4}")

#9. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
l5 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
l6 =" ".join(l5)
print(l6)

#10. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
l7 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
l7.insert(2,"new_value")
del l7[6]
print(l7)