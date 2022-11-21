from constants import *

def print_board(board):
    print('\n'.join((' '.join(r) for r in board)))


def check_win(board):
    # column
    for x in range(SIZE_X):
        for y in range(SIZE_Y - FOUR + 1):
            if board[y][x] == CHAR_EMPTY:
                continue
            same = True
            for i in range(1, FOUR):
                if board[y + i][x] != board[y][x]:
                    same = False
                    break
            if same:
                return board[y][x]

    # row
    for x in range(SIZE_X - FOUR + 1):
        for y in range(SIZE_Y):
            if board[y][x] == CHAR_EMPTY:
                continue
            same = True
            for i in range(1, FOUR):
                if board[y][x + i] != board[y][x]:
                    same = False
                    break
            if same:
                return board[y][x]

    # diag SE
    for x in range(SIZE_X - FOUR + 1):
        for y in range(SIZE_Y - FOUR + 1):
            if board[y][x] == CHAR_EMPTY:
                continue
            same = True
            for i in range(1, FOUR):
                if board[y + i][x + i] != board[y][x]:
                    same = False
                    break
            if same:
                return board[y][x]

    # diag SW
    for x in range(FOUR - 1, SIZE_X):
        for y in range(SIZE_Y - FOUR + 1):
            if board[y][x] == CHAR_EMPTY:
                continue
            same = True
            for i in range(1, FOUR):
                if board[y + i][x - i] != board[y][x]:
                    same = False
                    break
            if same:
                return board[y][x]

    return None

def copy_board(board):
    boardState = board
    return boardState    

def sim_move(board, col, pChar):
    if board[0][col] != CHAR_EMPTY:
            raise Exception(f'Column {col} is already full!')
    for y in range(SIZE_Y):
        if y >= SIZE_Y - 1 or board[y + 1][col] != CHAR_EMPTY:
            break
    board[y][col] = pChar
    return board




    
