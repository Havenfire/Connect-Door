from functools import cached_property, lru_cache
import random
import sys

from constants import *

def print_board(board):
    print('utils.print_board(board) is deprecated, please use board.print() instead.', file=sys.stderr)
    return board.print()


def check_win(board):
    print('utils.check_win(board) is deprecated, please use board.check_win() instead.', file=sys.stderr)
    return board.check_win()

def copy_board(board):
    print('utils.copy_board(board) is deprecated, please use board.copy() instead.', file=sys.stderr)
    boardState = board
    return boardState

def sim_move(board, col, pChar):
    
    for y in range(SIZE_Y):
        if y >= SIZE_Y - 1 or board[y + 1][col] != CHAR_EMPTY:
            break
    board[y][col] = pChar
    return board

def argmax(l):
    best_i = [-1]
    best_v = -float('inf')
    for i, v in enumerate(l):
        if v == best_v:
            best_i.append(i)
        if v > best_v:
            best_v = v
            best_i = [i]
    return random.choice(best_i)


@lru_cache(maxsize=None)
def win_lines():
    lines = []
    # column
    for x in range(SIZE_X):
        for y in range(SIZE_Y - FOUR + 1):
            lines.append(tuple((x, y + i) for i in range(FOUR)))
    # row
    for x in range(SIZE_X - FOUR + 1):
        for y in range(SIZE_Y):
            lines.append(tuple((x + i, y) for i in range(FOUR)))
    # diag SE
    for x in range(SIZE_X - FOUR + 1):
        for y in range(SIZE_Y - FOUR + 1):
            lines.append(tuple((x + i, y + i) for i in range(FOUR)))
    # diag SW
    for x in range(FOUR - 1, SIZE_X):
        for y in range(SIZE_Y - FOUR + 1):
            lines.append(tuple((x - i, y + i) for i in range(FOUR)))
    
    return lines