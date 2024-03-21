"""
Tic Tac Toe Player
"""

import math
import copy

from exception_scripts.exceptions import InvalidAction

X = "X"
O = "O"
EMPTY = None

current_player = 0 # if its even then its x turn to move.

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    pointers = {"X": 0, "O": 0} # it counts how many Xs are there and Os

    for line in board:
        for symbol in line:
            if symbol == "X":
                pointers["X"] +=1
            elif symbol == "O":
                pointers["O"] +=1
            else:
                continue

    if pointers["X"] > pointers["O"]:
        return "O"

    return "X"
        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i, line in enumerate(board):
        for j, symbol in enumerate(line):
            if symbol == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    updated_board = copy.deepcopy(board)
    
    next_step = player(updated_board) # getting players move (whether its x or o)


    if updated_board[action[0]][action[1]] == EMPTY:
        updated_board[action[0]][action[1]] = next_step

    else:
        print("Invalid action taken")
        raise InvalidAction
        
    return updated_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    xcounter = 0
    ocounter = 0

    #getting winner in a row
    for i,line in enumerate(board):
        xcounter = 0 
        ocounter = 0
        for j,symbol in enumerate(line):
            if symbol == "X":
                xcounter+=1
            elif symbol == "O":
                ocounter+=1
            
            if xcounter == 3:
                print("row win")

                return "X"
            elif ocounter ==3:
                print("row win")

                return "O"            

    #columns
    for i in range(len(board)):
        xcounter = 0
        ocounter = 0
        current_column = column(board, i)

        for j in current_column:
            if j == "X":
                xcounter +=1
            elif j == "O":
                ocounter+=1

            if xcounter == 3:
                print("column win")
                return "X"
            
            elif ocounter == 3:
                print("column win")

                return "O"

    #diagonally 
    xcounter = 0
    ocounter = 0
    for i in range(0,3):
        if board[i][i] == "X":
            xcounter+=1

        elif board[i][i] == "O":
            ocounter+=1
        
        if xcounter == 3:
            print("horizontal +1")
            return "X"
            
        elif ocounter == 3:
            return "O"


    ocounter = 0
    xcounter = 0 

    #diagonally -1
    if board[0][-1] == board[1][1] == board[2][0]:
        if board [0][-1] == "X":
            return "X"
            
        elif board[0][-1]=="O":
            return "O"

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True

    if is_empty(board):
        return False
    else:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    game_winner = winner(board)


    if game_winner == "X":
        return 1
    elif game_winner == "O":
        return -1

    if game_winner is None:
        return 0

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    current_player = player(board)

    if current_player == "X":
        optimal_play = max_value(board)[1]
        return optimal_play
    else:
        optimal_play = min_value(board)[1]
        return optimal_play


def max_value(board):
    if terminal(board):
        print("game is over")
        return [utility(board), None]
        
    v = float("-inf")
    
    for action in actions(board):
        updated_board = result(board, action)
        value = min_value(updated_board)[0]
        print("Max Value:", value, "Action:", action)
        if value > v:
            v = value
            best_action = action

    return [v,best_action]
    
def min_value(board):
    if terminal(board):
        print("game is over")
        return [utility(board), None]
        
    v = float("inf")
    best_action = None

    for action in actions(board):
        updated_board = result(board, action)
        value = max_value(updated_board)[0]
        print("Min Value:", value, "Action:", action)
        if value < v:
            v = value
            best_action = action

    return [v, best_action]


def column(matrix, colum_number):
    return [row[colum_number] for row in matrix]

def is_empty(board): # checks if all game cells have been filled out 
    for i,line in enumerate(board): # returns true if game cells are ALL EMPTY
        for j, symbol in enumerate(line):
            if symbol == EMPTY:
                return True
    return False