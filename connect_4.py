import copy
from functools import lru_cache

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

        self.wins = []


    def update_win_cache(self, updated_spot):
        for line in win_lines_per_spot()[updated_spot[1]][updated_spot[0]]:
            char = self._board[line[0][1]][line[0][0]]
            if char == CHAR_EMPTY:
                continue
            same = True
            for spot in line[1:]:
                if self._board[spot[1]][spot[0]] != char:
                    same = False
                    break
            if same:
                self.wins.append((char, line))

    def check_win(self):
        return None if len(self.wins) == 0 else self.wins[0][0]

    def place_piece(self, col, char):
        if self._board[0][col] != CHAR_EMPTY:
            raise Exception(f'Column {col} is already full!')
        for y in range(SIZE_Y):
            if y >= SIZE_Y - 1 or self._board[y + 1][col] != CHAR_EMPTY:
                break
        self[y][col] = char
        self.update_win_cache((col, y))
        return int(y), int(col)

    def heights(self):
        h = [-1] * SIZE_X
        for x in range(SIZE_X):
            for y in range(SIZE_Y):
                if y >= SIZE_Y - 1 or self._board[y + 1][x] != CHAR_EMPTY:
                    break
            h[x] = y
        return h


    def __setitem__(self, index, value):
        self._board.__setitem__(index, value)

    def __getitem__(self, index):
        return self._board.__getitem__(index)

    def print(self):
        if SHOULD_PRINT:
            print3f('\n'.join((' '.join(r) for r in self._board)))

    def copy(self):
        new_board = copy.copy(self)
        new_board._board = [r[:] for r in new_board._board]
        new_board.wins = new_board.wins[:]
        return new_board


def main_loop(board):
    players = [Human(CHAR_0), HeuristicAgent(CHAR_1)]
    if random.choice([True, False]):
        players = players[::-1]
    for i in range(SIZE_X * SIZE_Y):
        curr_player = players[i % len(players)]
        print3f(f'Turn {i}, {curr_player}')
        col = curr_player.take_turn(board)
        board.place_piece(col, curr_player.char)
        print3f(f'Placed in column {col + 1}')
        board.print()
        winner = board.check_win()
        if winner:
            print3f(f'{winner} has won!')
            return winner
        print3f('')


if __name__ == '__main__':
    board = initialize()
    board.print()
    main_loop(board)
