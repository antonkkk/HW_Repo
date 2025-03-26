# 8.
def print_board(board):
    for row in board:
        print(" ".join(row))


def check_win(board, player):
    return (any(all(cell == player for cell in row) for row in board) or
            any(all(board[row][col] == player for row in range(5)) for col in range(5)) or
            all(board[i][i] == player for i in range(5)) or
            all(board[i][4 - i] == player for i in range(5)))


def check_full(board):
    return all(cell != "." for row in board for cell in row)


def play_game():
    board = [["." for _ in range(5)] for _ in range(5)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Игрок {current_player}, ваш ход:")
        row = int(input("Введите номер строки (1-5): ")) - 1
        col = int(input("Введите номер столбца (1-5): ")) - 1

        if 0 <= row < 5 and 0 <= col < 5 and board[row][col] == ".":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            if check_full(board):
                print_board(board)
                print("Ничья!")
                break
            turn += 1
        else:
            print("Попробуйте снова.")


play_game()
