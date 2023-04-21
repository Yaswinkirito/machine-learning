from tictactoe import winner
X = "X"
O = "O"
EMPTY = None
a=[[X, O, X],
            [O, O, X],
            [O, EMPTY, X]]
print(winner(a))