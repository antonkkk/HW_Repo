# 1
name = "www.my_site.com#about"
print(name.replace("#","/"))

# 2
word = "word"
print(word + "ing")

# 3
names = "Ivanou Ivan"
words = names.split()
reversed_names = ' '.join(words[::-1])
print(reversed_names)

# 4
text = " Hello World "
print(text.strip())

# 5
city = "pARiS"
new_city = city.capitalize()
print(new_city)

# 6
s1 = "Robin Singh"
l1 = s1.split()
print(l1)

# 7
s2 = "I love arrays they are my favorite"
l2 = s2.split()
print(l2)

# 8
l3 = ["Ivan", "Ivanou"]
l4 = ' '.join(l3)
s3 = "Minsk"
s4 = "Belarus"
print(f"Привет, {l4}! Добро пожаловать в {s3} {s4}")

# 9
l5 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
l6 = " ".join(l5)
print(l6)

# 10
l7 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
l7.insert(2,"new_value")
del l7[6]
print(l7)
