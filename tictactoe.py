# --------- Global Variables -----------

# Will hold our game board data
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# Lets us know if the game is over yet
game_still_going = True

game_again = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def main():
    # WELCOMING
    print("Welcome to the Tic Tac Toe from COURSE CSE210")
    print("Enjoy it!")
    # Show the initial game board
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:

            # Handle a turn
            handle_turn(current_player)

            # Check if the game is over
            check_if_game_over()

            # Flip to the other player
            flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
        print("THANKS FOR PLAYING !!")
    elif winner == None:
        print("Tie.")
        print("THANKS FOR PLAYING !!")

    again = input("Do you want revenge? \n Press Y / N ")

    if again == "y" or again == "Y":

        # THIS FUNCTION RESTARTS THE BOARD
        restart_game()
        # WELCOMING
        print("Welcome to the Tic Tac Toe from COURSE CSE210")
        print("Enjoy it!")
        # Show the initial game board
        display_board()

        while game_still_going:

            # Handle a turn
            handle_turn(current_player)

            # Check if the game is over
            check_if_game_over()

            # Flip to the other player
            flip_player()

        if winner == "X" or winner == "O":
                print(winner + " won.")
                print("THANKS FOR PLAYING !!")
        elif winner == None:
                print("Tie.")
                print("THANKS FOR PLAYING !!")
                
        

    elif again == "n" or again == "N":
        print("THANKS FOR PLAYING !!")

# Display the game board to the screen
def display_board():
    print("\n")
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "_":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


# Check if the game is over
def check_if_game_over():
    check_winner()
    check_tie()


# Check to see if somebody has won
def check_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "_" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"

def restart_game():
    board[0] = "_"
    board[1] = "_"
    board[2] = "_"
    board[3] = "_"
    board[4] = "_"
    board[5] = "_"
    board[6] = "_"
    board[7] = "_"
    board[8] = "_"


# ------------ Start Execution -------------
# Play a game of tic tac toe
if __name__ == '__main__':
    main()
