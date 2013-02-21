
from random import choice

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
    return choice(player_list)

def determine_second_player_identity(first_player):
    return get_next_player(first_player, playerX, playerO)

def get_next_player(player, first_player, second_player):
    return first_player if player == second_player else second_player

def make_move(player):
    player_marks = {playerX : 'x', playerO : 'O'}
    return player_marks[player]

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
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for pos1, pos2, pos3 in winning_combinations:
        for mark in "XO":
            if current_board[pos1] == current_board[pos2] == current_board[pos3]:
                return True
    return False

def handle_next_move(player, first_player, second_player, board):
    move_selection = raw_input ("Ok, %s, make your move. \n" %player)
    verfied_move_selection = verify_numerical_selection_for_move(move_selection)

    if legal_move(board, verfied_move_selection):
        board[verfied_move_selection] = make_move(player)
        display_board(board)
        if there_is_a_winner(board):
            print "Game over! The winner is %s" %player
        elif game_over(board):
            print "Game over! Sadly, no winner. Please try again."
        else:
            handle_next_move(get_next_player(player, first_player, second_player), first_player, second_player, board)
    else:
        print "That was an illegal move, let's try again..."
        handle_next_move(player, first_player, second_player, board)

def play_game(first_player, second_player, board):
    #first time through
    move_selection = raw_input ("Ok, %s, make your first move by selecting a number on the board \nto move to. \n" %first_player)
    verfied_move_selection = verify_numerical_selection_for_move(move_selection)
    board[verfied_move_selection] = make_move(first_player)
    display_board(board)

    #subsequent moves
    handle_next_move(get_next_player(first_player, first_player, second_player), first_player, second_player, board)


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
second_player = determine_second_player_identity(first_player)
board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
display_board(board)

#play game
play_game(first_player, second_player, board)








