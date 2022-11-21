import random

from constants import *
from utils import *

class Agent:
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        col = random.randrange(SIZE_X)
        while board[0][col] != CHAR_EMPTY:
            col = random.randrange(SIZE_X)
        return col

    def __repr__(self):
        return f'Agent({self.char})'

class See3PO(Agent):
    def take_turn(self, board):
        
        for col in range[SIZE_X]:
            if(board[0][col] != CHAR_EMPTY):
                if check_win != None:
                    return col
        return super().take_turn(self, board)
    


class MidLover(Agent):
    def take_turn(self, board):
        prio = [3, 2, 4, 1, 5, 0, 6]
        for col in prio:
            if board[0][col] != CHAR_EMPTY:
                return col


class CenterLover:
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        prio = self.createPrio

        for i in range[SIZE_X]:
            board
            

    def createPrio():
        prio = [SIZE_X][SIZE_Y]
        x_vals = [1, 2, 3, 4, 3, 2, 1]
        y_vals = [1, 2, 3, 3, 2, 1]

        for i in range[0, SIZE_X]:
            for j in range[0, SIZE_Y]:
                prio[i][j] = x_vals[i] * y_vals[j]
        return prio



    def __repr__(self):
        return f'Agent({self.char})'