import random

## constants
SIZE_X = 7
SIZE_Y = 6
CHAR_EMPTY = '_'
CHAR_0 = 'O'
CHAR_1 = 'X'

def initialize():
    board = []
    for i in range(SIZE_Y):
        board.append([CHAR_EMPTY] * SIZE_X)

    return board


def print_board(board):
    print('\n'.join((' '.join(r) for r in board)))


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

def main_loop(board):
    players = [Agent(CHAR_0), Agent(CHAR_1)]
    for i in range(SIZE_X * SIZE_Y):
        curr_player = players[i % len(players)]
        print(f'turn {i}, {curr_player}')
        col = curr_player.take_turn(board)
        for y in range(SIZE_Y):
            if y >= SIZE_Y - 1 or board[y + 1][col] != CHAR_EMPTY:
                break
        board[y][col] = curr_player.char
        print(f'placed at {y} {col}')
        print_board(board)
        print('')

if __name__ == '__main__':
    board = initialize()
    print_board(board)
    main_loop(board)