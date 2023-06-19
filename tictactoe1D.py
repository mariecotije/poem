# import module for computer choice
from random import randrange 


# step 1: evaluate if the game has ended
def evaluate_board(board):
    """A function that accepts the string with the board of 1D tic-tac-toe as argument
    and returns one character based on the state of the game."""
    
    if "xxx" in board: # player won
        result = "x"
    elif "ooo" in board: # PC won
        result = "o"
    elif "_" not in board: # the board is full and there is no winner
        print(board)
        result = "!"
    else: # game coninues
        result = "-"

    return result


# step 2: move function
def move(board, mark, position):
    """ A function that returns the game board with the given mark in the given position."""
    
    board = board[:position] + mark + board[position + 1:] # the board is devided to bustrings. Firsts sustring is from beginning to chosen position.
    # the second substring is from position +1 till the end. 
    return board


# step 3: make sure a user will not insert no negative numbers, too large numbers, spot is not empty
def validate_position(position, board):
    """A function that checks that a player/PC doesn't choose a number out of board range or already taken positions."""
    
    if position < 0 or position > 19:
        print("Number is outside of range 0-19")
        return False
    elif board[position] != "_":
        print("This position is occupied")
        return False
    else:
        return True # if any of conditions above is not met, the position is ok to be occupied by the user or PC


# player move
def player_move(board):
    is_valid = False # if the position is occupied or out of range, a player must choose another position
    while is_valid == False:  # position is invalid
        user_input = input("Enter your move position:")
        if user_input.isdigit(): #validation for the inserted character in the input is a number
            position = int(user_input) # user input will be used as an argument for position to take
            is_valid = validate_position(position, board) # is_valid == True
        else:
            print("Invalid input")

    return move(board, "x", position)


# step 4: pc choice function
def pc_move(board):
    """A funtion that takes board as an argument an returnes updated board with the random PC choice."""

    is_valid = False # the same validation process as for the player to make sure the position is not occupied
    while is_valid == False:  # position is invalid
        pc_input = randrange(0, 20)
        position = pc_input
        is_valid = validate_position(position, board) #if not occupied, the is_valid is True
        print("PC choice is: ", position) #shows whic position PC chosed

    return move(board, "o", position)


# step 5: function for starting game
def tictactoe_1D():
    """ A funtion for 1D tic-tac-toe, player versus PC."""
    
    # create board
    board = "_" * 20
    print(board)
    
    # evaluate board
    while evaluate_board(board) == "-":
        # call player move
        board = player_move(board)
        print(board)
        if evaluate_board(board) == "x": # if there already is "xxx", makes no sense to ask computer. The loop must be finished.
            break
        # call pc_move
        board = pc_move(board)
        print(board)

    game_result = evaluate_board(board) # print play result
    if game_result == "x":
        print("Player won")
    elif game_result == "o":
        print("PC won")
    elif game_result == "!":
        print("It's a tie")
    else:
        print("Unknown state")


tictactoe_1D()
