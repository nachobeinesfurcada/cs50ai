from tictactoe import initial_state, player, actions, result, winner, terminal

X = "X"
O = "O"

EMPTY = None

board = [[X, O, O],
        [EMPTY, EMPTY, X],
        [O, O, X]]


print(terminal(board))