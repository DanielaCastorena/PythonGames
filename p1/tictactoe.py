#Daniela Castorena
#simple tic-tac-toe 2 player game written in python

def print_board(board):
    for i in range(3):
        print("+---+---+---+")
        print("| {} | {} | {} |".format(board[i][0], board[i][1], board[i][2]))
    print("+---+---+---+")

def check_winner(board):
    #3 in a row?
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    #3 down a column?
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    #diagonal win?
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player {}: ".format(player)))
        col = int(input("Enter column (0, 1, or 2) for player {}: ".format(player)))

        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player {} wins!".format(player))
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("That position is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
