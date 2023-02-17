from tictactoe import initial_state, player, actions, result, winner

X = "X"
O = "O"

EMPTY = None

board = [[X, O, O],
        [O, O, X],
        [O, O, X]]


print(winner(board))