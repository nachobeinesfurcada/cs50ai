"""
Tic Tac Toe Player
"""

import math
from util import Node, StackFrontier, QueueFrontier
import copy

X = "X"
O = "O"
EMPTY = None

moves = 2

def initial_state():
    """
    Returns starting state of the board.
    """
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    return board


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player_turn = 0

    if initial_state:
        return X
    elif (moves % 2) != 0:
        return O
    elif (moves % 2) == 0:
        return X
    else: 
        return 0
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    # loop over all board positions to check for not empty
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if column is EMPTY:
                actions.append((row_index, column_index))

    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # make a copy of board
    board_copy = copy.deepcopy(board)

    # if action is not valid
    if action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0:
        raise Exception
    else:    
        if (moves % 2) != 0:
            board_copy[action[0]][action[1]] = O
        elif (moves % 2) == 0:
            board_copy[action[0]][action[1]] = X
        return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal checking
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == X:
            return X
        elif board[row][0] == board[row][1] == board[row][2] == O:
            return O

    # virtical checking
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X
        elif board[0][col] == board[1][col] == board[2][col] == O:
            return O

    # diagonal checking
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
