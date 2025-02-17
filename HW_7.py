# 1.
number_computer = "1234"
correct = False
while not correct:
    number_player = input("Enter 4 digits value with unique numbers")
    if len(number_player) != 4:
        print("Not 4 digits, please, try again!")
        continue
    elif not number_player.isdigit():
        print("Not digits, please, try again!")
        continue
    elif len(set(number_player)) != 4:
        print("Not unique numbers, please, try again")
        continue
    elif number_player == number_computer:
        print("You win")
        correct = True
    else:
        bulls = 0
        cows = 0
        for i in range(4):
            if number_player[i] == number_computer[i]:
                bulls +=1
            elif number_player[i] in number_computer:
                cows +=1
        print(f"Bulls: {bulls}, Cows: {cows}")

# 2.
N = 10
for i in range(N):
    for j in range(N - i - 1):
        print(" ", end = "")
    for k in range(i * 2 + 1):
        print("*", end = "")
    print()

# 3.
l = [6, 2, 3, 8]
l_a = []
for i in range(2,9):
    l_a.append(i)
l = set(l)
l_a = set(l_a)
l_f = l.symmetric_difference(l_a)
print(len(l_f))
