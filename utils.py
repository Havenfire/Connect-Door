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

