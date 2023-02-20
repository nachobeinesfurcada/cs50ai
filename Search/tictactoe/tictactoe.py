"""
Tic Tac Toe Player
"""

import copy

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
    """
    #check for quantity of plays made
    moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                moves += 1

    # check for moves and define next player
    if board == initial_state():
        return X
    if moves % 2 == 1:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # return number of places where the next move can be
    actions = set()
    for l in range(3):
        for k in range(3):
            if board[l][k] == EMPTY:
                actions.add((l,k))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    # make a copy and return it with the new action from player
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


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

    # first diagonal checking
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    # second diagonal checking
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # pretty straight forward
    if winner(board) is not None:
        return True

    for l in range(3):
        for k in range(3):
            if  board[l][k] == None:
                return False
    return True

    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The maximizing player picks action a in Actions(s)
    # that produces the highest value of Min-Value(Result(s, a)).

    # The minimizing player picks action a in Actions(s)
    # that produces the lowest value of Max-Value(Result(s, a)).

    if terminal(board):
        return None

    maximum = float(-1000)
    minimum = float(1000)

    if player(board) == X:
        return max_value(board, maximum, minimum)[1]
    else:
        return min_value(board, maximum, minimum)[1]

# defining a function that recursively calculates the maximum value for X to play
def max_value(board, maximum, minimum):

    move = None

    if terminal(board):
        return [utility(board), None]

    # defining a very small value
    v = float(-1000)

    for action in actions(board):
        play = min_value(result(board, action), maximum, minimum)[0]
        maximum = max(maximum, play)
        if play > v:
            v = play
            move = action
        if maximum >= minimum:
            break

    return [v, move]

# defining a function that recursively calculates the minimum value for O to play
def min_value(board, maximum, minimum):
    move = None

    if terminal(board):
        return [utility(board), None]

    # defining a very big value
    v = float(1000)

    # loop that calls min_value function and compares which one is smaller
    for action in actions(board):
        play = max_value(result(board, action), maximum, minimum)[0]
        minimum = min(minimum, play)
        if play < v:
            v = play
            move = action
        if maximum >= minimum:
            break

    return [v, move]
