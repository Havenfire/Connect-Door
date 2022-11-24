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

def print3f(*args, **kwargs):
    if SHOULD_PRINT:
        print(*args, **kwargs)


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
            line = tuple({0 : x, 1 : y + i} for i in range(FOUR))
            lines.append(line)
    # row
    for x in range(SIZE_X - FOUR + 1):
        for y in range(SIZE_Y):
            line = tuple({0 : x + i, 1 : y} for i in range(FOUR))
            lines.append(line)
    # diag SE
    for x in range(SIZE_X - FOUR + 1):
        for y in range(SIZE_Y - FOUR + 1):
            line = tuple({0 : x + i, 1 : y + i} for i in range(FOUR))
            lines.append(line)
    # diag SW
    for x in range(FOUR - 1, SIZE_X):
        for y in range(SIZE_Y - FOUR + 1):
            line = tuple({0 : x - i, 1 : y + i} for i in range(FOUR))
            lines.append(line)

    return lines

@lru_cache(maxsize=None)
def win_lines_per_spot():
    lines_per_spot = {y : {x : [] for x in range(SIZE_X)} for y in range(SIZE_Y)}
    for line in win_lines():
        for spot in line:
            lines_per_spot[spot[1]][spot[0]].append(line)
    return lines_per_spot
