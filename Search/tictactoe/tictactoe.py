"""
Tic Tac Toe Player
"""

import math
from util import Node, StackFrontier, QueueFrontier
import copy

X = "X"
O = "O"
EMPTY = None


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
    moves = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                moves += 1

    if board == initial_state():
        return X
    if moves % 2 == 1:
        return O
    else:
        return X
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    # loop over all board positions to check for not empty
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if column == EMPTY:
                actions.add((row_index, column_index))

    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # if action is not valid
    if action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0:
        raise Exception

    # make a copy of board
    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = player(board)

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

    # vertical checking
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
    if winner(board) == X or winner(board) == O or winner(board) == None:
        return True
    elif winner(board) is False:
        False

    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) is X:
        return 1
    if winner(board) is O:
        return -1
    if winner(board) is False:
        return O

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return max_value(board, Max, Min)[1]
    else:
        return min_value(board, Max, Min)[1]


    raise NotImplementedError


def max_value(board):
    
    move = None

    if terminal(board):
        return [utility(board), None];

    v = float('-inf')

    for action in actions(board):
        test = min_value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];


def min_value(board):

    move = None

    if terminal(board):
        return [utility(board), None];

    v = float('inf')

    for action in actions(board):
        test = max_value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

