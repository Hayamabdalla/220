"""
Name: <hayam Abdalla>
lab10.py
"""


def build():
    return list(range(1, 10))


def display(board):
    for i in range(3):
        n = i*3
        print(board[n], board[n+1], board[n+2], sep="|")
        print(10*"_")


def place(board, position, piece):
    if board[position-1] == "x" or board[position-1] == "o":
        return
    else:
        board[position-1] = piece


def game_won(board, piece):
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    if board[0] == piece:
        if board[1] == piece:
            if board[2] == piece:
                return True
    if board[3] == piece:
        if board[4] == piece:
            if board[5] == piece:
                return True
    if board[6] == piece:
        if board[7] == piece:
            if board[8] == piece:
                return True
    if board[1] == piece:
        if board[4] == piece:
            if board[7] == piece:
                return True
    else:
        return False


def legal(board, position):
    if(position >= 1, position <= 9) and (board[position - 1] == position):
        return True
    return False


def over(board):
    if game_won(board, "x"):
        return True
    elif game_won(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i+1:
                return False
            # return True


def play_game():
    board = build()
    display(board)
    turn = 1

    while True:

        position = eval(input("enter position: "))
        if legal(board, position):
            if (turn % 2) == 0:
                place(board, position, "x")
                display(board)
                if over(board):
                    if game_won(board, "o"):
                        print("o won")
                        break

                    if game_won(board, "x"):
                        print("x won")

                    else:
                        print("tie")
                        break
            elif (turn % 2) == 1:
                place(board, position, "o")
                display(board)
                if over(board):
                    if game_won(board, "o"):
                        print("o won")
                        break

                    if game_won(board, "x"):
                        print("x won")

                    else:
                        print("tie")
                        break

        turn += 1


def main():
    play_game()


main()
