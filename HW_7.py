# 1.
number_computer = "1234"
correct = False
while not correct:
    number_player = input("Enter 4 digits value with unique numbers")
    if len(number_player) != 4:
        print("Not 4 digits, please, try again!")
        continue
    if not number_player.isdigit():
        print("Not digits, please, try again!")
        continue
    if len(set(number_player)) != 4:
        print("Not unique numbers, please, try again")
        continue
    if number_player == number_computer:
        print("You win")
        correct = True
    else:
        bulls = 0
        cows = 0
        for i in range(4):
            if number_player[i] == number_computer[i]:
                bulls += 1
            elif number_player[i] in number_computer:
                cows += 1
        print(f"Bulls: {bulls}, Cows: {cows}")

# 2.
N = 10
for i in range(N):
    for j in range(N - i - 1):
        print(" ", end="")
    for k in range(i * 2 + 1):
        print("*", end="")
    print()

# 3.
list_a = [6, 2, 3, 8]
list_b = []
for i in range(2, 9):
    list_b.append(i)
list_a = set(list_a)
list_b = set(list_b)
list_c = list_a.symmetric_difference(list_b)
print(len(list_c))
