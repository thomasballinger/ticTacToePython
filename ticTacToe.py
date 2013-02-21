
playerX = "player X"
playerO = "player O"
def welcome_to_new_game():
    print "Welcome to ticTacToe."
    display_board([None, None, None]*3)
    print "Let's begin by choosing player X or player O to begin the game."
    raw_input("Press return to begin this game... ")
    first_player = choose_starting_player()
    print "Great, the first player is %s" %first_player
    return first_player

def choose_starting_player():
    player_list = [playerX, playerO]
    from random import choice
    return choice(player_list)

def determine_second_player_identity():
    if first_player == playerX:
        second_player = playerO
    else:
        second_player = playerX
    return second_player

def get_next_player():
    global current_player
    if current_player == first_player:
        current_player =  second_player
    else:
        current_player = first_player
    return current_player

def make_move(the_current_player):
    board_marker = ""
    if the_current_player == playerX:
        board_marker = "X"
    else:
        board_marker = "O"
    return board_marker

def verify_numerical_selection_for_move(user_move_input):
    if not (str.isdigit(user_move_input)):
        user_move_input = raw_input("Please enter a valid number!\n")
        return verify_numerical_selection_for_move(user_move_input)
    user_move_input = int(user_move_input)
    if user_move_input > 8 or user_move_input < 0:
        user_move_input = raw_input("Please enter a number between 0 and 8!\n")
        return verify_numerical_selection_for_move(user_move_input)
    else:
        return user_move_input

def legal_move(current_board, current_move_selection):
    if current_board[current_move_selection] == "X" or current_board[current_move_selection] == "O":
        return False
    else:
        return True

def game_over(current_board):
    for item in current_board:
        if (str.isdigit(item)):
            return False
    print "Game Over"
    return True

def there_is_a_winner(current_board):

    if (current_board[0] == "X" and current_board[1] == "X" and current_board[2] == "X") or (current_board[0] == "O" and current_board[1] == "O" and current_board[2] == "O"):
        return True
    if (current_board[3] == "X" and current_board[4] == "X" and current_board[5] == "X") or (current_board[3] == "O" and current_board[4] == "O" and current_board[5] == "O"):
        return True
    if (current_board[6] == "X" and current_board[7] == "X" and current_board[8] == "X") or (current_board[6] == "O" and current_board[7] == "O" and current_board[8] == "O"):
        return True
    if (current_board[0] == "X" and current_board[3] == "X" and current_board[6] == "X") or (current_board[0] == "O" and current_board[3] == "O" and current_board[6] == "O"):
        return True
    if (current_board[1] == "X" and current_board[4] == "X" and current_board[7] == "X") or (current_board[1] == "O" and current_board[4] == "O" and current_board[7] == "O"):
        return True
    if (current_board[2] == "X" and current_board[5] == "X" and current_board[8] == "X") or (current_board[2] == "O" and current_board[5] == "O" and current_board[8] == "O"):
        return True
    if (current_board[0] == "X" and current_board[4] == "X" and current_board[8] == "X") or (current_board[0] == "O" and current_board[4] == "O" and current_board[8] == "O"):
        return True
    if (current_board[2] == "X" and current_board[4] == "X" and current_board[6] == "X") or (current_board[2] == "O" and current_board[4] == "O" and current_board[6] == "O"):
        return True
    else:
        return False

def handle_next_move(player):
    move_selection = raw_input ("Ok, %s, make your move. \n" %player)
    verfied_move_selection = verify_numerical_selection_for_move(move_selection)

    if legal_move(game_board_in_play, verfied_move_selection):
        game_board_in_play[verfied_move_selection] = make_move(current_player)
        display_board(game_board_in_play)
        if there_is_a_winner(game_board_in_play):
            print "Game over! The winner is %s" %current_player
        elif game_over(game_board_in_play):
            print "Game over! Sadly, no winner. Please try again."
        else:
            handle_next_move(get_next_player())
    else:
        print "That was an illegal move, let's try again..."
        handle_next_move(current_player)

def play_game():
    #first time through
    move_selection = raw_input ("Ok, %s, make your first move by selecting a number on the board \nto move to. \n" %current_player)
    verfied_move_selection = verify_numerical_selection_for_move(move_selection)
    game_board_in_play[verfied_move_selection] = make_move(current_player)
    display_board(game_board_in_play)

    #subsequent games
    handle_next_move(get_next_player())


def display_board(boardList):
    board = []

    for item in boardList: #for the collection of items in board list, append the empty board
        if item is None:
            board.append(" ")
        else:
            board.append(item)

    print " {} | {} | {} ".format(board[0], board[1], board[2]) #using a format string, append the print statements with the new contents of board
    print "---+---+---"
    print " {} | {} | {} ".format(board[3], board[4], board[5])
    print "---+---+---"
    print " {} | {} | {} ".format(board[6], board[7], board[8])


#program begins here

#initial setup for new game
first_player = welcome_to_new_game()
second_player = determine_second_player_identity()
current_player = first_player
game_board_in_play = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
display_board(game_board_in_play)

#play game
play_game()








