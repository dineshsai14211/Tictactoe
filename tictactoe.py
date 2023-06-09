# Tictactoe
import numpy as np

def create_board():
    return np.array([[' ']*3]*3)

def printb(board):
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

def win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def boardfull(board):
    return ' ' not in board

def startgame():
    scorecard = {'X': 0, 'O': 0, 'Draw': 0}
    while True:
        board = create_board()
        current_player = 'X'
        game_over = False

        print("New Game!")
        printb(board)

        while not game_over:
            print(f"\nPlayer '{current_player}', it's your turn.")
            l=[0,1,2]
            row = int(input("Enter the row number (0, 1, or 2): "))

            if row in l:
              col = int(input("Enter the column number (0, 1, or 2): "))
              if col in l:
                if board[row][col] == ' ':
                  board[row][col] = current_player
                  printb(board)

                if win(board, current_player):
                    print(f"*************Player '{current_player}' wins!***************")
                    scorecard[current_player] += 1
                    game_over = True
                elif boardfull(board):
                    print("The game ends in a draw!")
                    scorecard['Draw'] += 1
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")

        print("Scorecard:")
        print(f"Player 'X': {scorecard['X']} wins")
        print(f"Player 'O': {scorecard['O']} wins")
        print(f"Draw: {scorecard['Draw']}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

startgame()
