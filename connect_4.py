

from agents import *
from constants import *
from utils import *


def initialize():
    board = []
    for i in range(SIZE_Y):
        board.append([CHAR_EMPTY] * SIZE_X)

    return board


def main_loop(board):
    players = [Agent(CHAR_0), Human(CHAR_1)]
    for i in range(SIZE_X * SIZE_Y):
        curr_player = players[i % len(players)]
        print(f'turn {i}, {curr_player}')
        col = curr_player.take_turn(board)
        if board[0][col] != CHAR_EMPTY:
            raise Exception(f'Column {col} is already full!')
        for y in range(SIZE_Y):
            if y >= SIZE_Y - 1 or board[y + 1][col] != CHAR_EMPTY:
                break
        board[y][col] = curr_player.char
        print(f'placed at {y} {col}')
        print_board(board)
        winner = check_win(board)
        if winner:
            print(f'{winner} has won!')
            break
        print('')


if __name__ == '__main__':
    board = initialize()
    print_board(board)
    main_loop(board)
