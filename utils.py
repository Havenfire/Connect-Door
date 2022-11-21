import sys

from constants import *

def print_board(board):
    print('utils.print_board(board) is deprecated, please use board.print() instead.', file=sys.stderr)
    return board.print()


def check_win(board):
    print('utils.check_win(board) is deprecated, please use board.check_win() instead.', file=sys.stderr)
    return board.check_win()
