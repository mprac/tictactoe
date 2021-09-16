"""
Tic Tac Toe Player
"""

import math
import copy
import sys

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    
    1. Take a board state as input and return which players turn it is.
    2. In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    3. loop over list and count how many x and o on board. 
    """
    # Check if board is in initial_state
    if board == initial_state():
        return X 
    else:
        # Keep track of how many moves each player took
        x_moves = 0
        o_moves = 0
        # Loop over board list and count how many XO moves
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    x_moves += 1
                elif board[i][j] == O:
                    o_moves += 1
        # If X has more moves its O's turn otherwise its X's turn
        return O if x_moves > o_moves else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize set
    possible_actions = set()
    # Loop over board to check for empty results 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                # Add tuple to set of possible actions
                possible_actions.add((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    1. If action is not a valid action for the board, your program should raise an exception.
    2. original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    """
    # Create a deep copy of board
    boardcopy = copy.deepcopy(board)
    # If action is not valid raise an exception
    if action[0] not in range(3) or action[1] not in range(3):
        raise Exception("Out of range")
    else:
        boardcopy[action[0]][action[1]] = player(board)
    # Return new board
    return boardcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    1. One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    2. If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    """
    #  return 0[[0EMPTY, 1EMPTY, 2EMPTY],
    #         1[EMPTY, EMPTY, EMPTY],
    #         2[EMPTY, EMPTY, EMPTY]]
    # Check columns
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check rows
    elif all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board [0][2]
    else:
        return None    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    1. If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    """
    if any(None in x for x in board) and winner(board) is None:
        return False
    else:
        return True
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    1.he utility function should accept a terminal board as input and output the utility of the board.
    2.You may assume utility will only be called on a board if terminal(board) is True.
    """
    if winner(board) is None:
        return 0
    elif winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    The minimax function should take a board as input, and return the optimal move for the player to move on that board.

    1. The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    2. If the board is a terminal board, the minimax function should return None.
    3. Alpha-beta pruning

    MAX(X) aims to maximize the score 
    MIN(O) aims to minimize the score
    """
    if terminal(board):
        return None
    # return the optimal move for the player
    # possible outcomes 1(X wins) 0(No winner) -1(O wins)
    if player(board) == X:
        _ , action = max_value(board)
        return action
    elif player(board) == O:
        _ , action = min_value(board)
        return action

def max_value(board): # the X player wants to maximize the score
    """
    MAX picks action a in Actions(s) that produces the highest value of minValue(result(s,a))
    """
    if terminal(board):
        return utility(board), None
    else:
        v = -math.inf
        move = None
        for action in actions(board):
            val, _ = min_value(result(board, action))
            # Check if returned Value is less than v if not return v and current action
            if val > v:
                # Assign v the maximum value for future evaluation
                v = max(v,val)
                # Keep track of action
                move = action
                # If best move then return it
                if v == 1:
                    return v, move
        return v, move

def min_value(board): # the O player wants to minimze the score
    """
    MIN picks action a in Actions(s) that produces the smallest value of Max-Value(result(s,a))
    """
    if terminal(board):
        return utility(board), None
    else:
        v = math.inf
        move = None
        track = {}
        for action in actions(board):
            val, _ = max_value(result(board, action))
            # Check if returned Value is less than v if not return v and current action
            if val < v:
                # Assign v the minimum value for future evaluation
                v = min(v, val)
                # Keep track of action
                move = action
                # If best move then return it
                if v == -1:
                    return v, move
        return v, move

#testing
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])