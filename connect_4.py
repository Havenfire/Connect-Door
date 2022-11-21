import copy
from functools import cached_property

from agents import *
from constants import *
from utils import *


def initialize():
    board = Board(SIZE_X, SIZE_Y, [CHAR_EMPTY, CHAR_0, CHAR_1])

    return board


class Board:
    def __init__(self, size_x, size_y, chars):
        self.size_x = size_x
        self.size_y = size_y
        self.chars = chars
        
        self._board = []
        for _ in range(size_y):
            self._board.append([chars[0]] * size_x)

    @cached_property
    def win_lines(self):
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

    def get_wins(self):
        wins = []
        for line in self.win_lines:
            char = self[line[0][1]][line[0][0]]
            if char == CHAR_EMPTY:
                continue
            same = True
            for spot in line:
                if self[spot[1]][spot[0]] != char:
                    same = False
                    break
            if same:
                wins.append((char, line))

        return sorted(wins)

    def check_win(self):
        wins = self.get_wins()
        return None if len(wins) == 0 else wins[0][0]

    def place_piece(self, col, char):
        if self[0][col] != CHAR_EMPTY:
            raise Exception(f'Column {col} is already full!')
        for y in range(SIZE_Y):
            if y >= SIZE_Y - 1 or self[y + 1][col] != CHAR_EMPTY:
                break
        self[y][col] = char


    def __setitem__(self, index, value):
        self._board.__setitem__(index, value)

    def __getitem__(self, index):
        return self._board.__getitem__(index)

    def print(self):
        print('\n'.join((' '.join(r) for r in self._board)))

    def copy(self):
        new_board = copy.deepcopy(self)
        return new_board


def main_loop(board):
    players = [Agent(CHAR_0), See3PO(CHAR_1)]
    for i in range(SIZE_X * SIZE_Y):
        curr_player = players[i % len(players)]
        print(f'Turn {i}, {curr_player}')
        col = curr_player.take_turn(board)
        board.place_piece(col, curr_player.char)
        print(f'Placed in column {col + 1}')
        board.print()
        winner = board.check_win()
        if winner:
            print(f'{winner} has won!')
            break
        print('')


if __name__ == '__main__':
    board = initialize()
    print_board(board)
    main_loop(board)
