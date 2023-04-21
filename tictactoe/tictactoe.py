"""
Tic Tac Toe Player
"""

import math
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
    x_counter=0
    o_counter=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                x_counter+=1
            elif board[i][j]==O:
                o_counter+=1
    if x_counter>o_counter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                a.add((i,j))
    return a


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is not None:
        b=copy.deepcopy(board)
        b[action[0]][action[1]]=player(board)
        return b
    else:
        return board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2]!=None:
      
            return board[i][0]
    for i in range(3):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i]!=None:
            
            return board[0][i]
    
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]!=None:
        return board[2][2]
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]!=None:
        return board[2][0]
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    k=winner(board)
    if k==X:
        return 1
    elif k==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if player(board)==X:
        v,mov=maximise(board)
        return mov
    else:
        v,mov=minimise(board)
        return mov


def maximise(board):
    v=-math.inf
    mov=None
    if terminal(board):
        return utility(board),None
    for i in actions(board):
        a,act=minimise(result(board,i))
        if a>v:
            v=a
            mov=i
    return v,mov   


def minimise(board):
    v=math.inf
    mov=None
    if terminal(board):
        return utility(board),None
    for i in actions(board):
        a,act=maximise(result(board,i))
        if a<v:
            v=a
            mov=i
    return v,mov
