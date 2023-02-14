# Create function to display board

board = [" " for i in range(0, 9)]

def display_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


# Create a function for move by each player

def player_move(icon):

    if icon == "X":                                               # Assign icon to player numbers 1 & 2
        number = 1
    elif icon == "O":
        number = 2

    print("Its your turn player {}".format(number))
    print()
    choice = int(input("Enter your move (1-9) : ").strip())

    if board[choice-1] == " ":                                    # check if the place is already taken to avoid duplication of move
        board[choice-1] = icon
    else:
        print()
        print("This place is already taken!")
        print()


# Create a function to check the winner


def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon) or \
       (board[3]==icon and board[4]==icon and board[5]==icon) or \
       (board[6]==icon and board[7]==icon and board[8]==icon) or \
       (board[0]==icon and board[3]==icon and board[6]==icon) or \
       (board[1]==icon and board[4]==icon and board[7]==icon) or \
       (board[2]==icon and board[5]==icon and board[8]==icon) or \
       (board[0]==icon and board[4]==icon and board[8]==icon) or \
       (board[2]==icon and board[4]==icon and board[6]==icon):

        return True

    else:
        return False



# Create a function to check if there is a draw


def is_draw(icon):
    if " " not in board:
        return True
    else:
        return False



# Run the loop for move by players

while True:
    display_board()
    player_move("X")
    display_board()
    if is_victory("X"):
        print("Congratulations! Player 1 wins!")
        break
    elif is_draw("x"):
        print("Its a draw!")
        break

    display_board()

    player_move("O")
    if is_victory("O"):
        display_board()
        print("Congratulations! Player 2 wins!")
        break
    elif is_draw("O"):
        print("Its a draw!")
        break




