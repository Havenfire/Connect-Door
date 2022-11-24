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

    def other_chars(self, board):
        return list(set(board.chars) - set((self.char, CHAR_EMPTY)))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.char})'


class Copycat(Agent):
    def take_turn(self, board):
        for x in range(SIZE_X):
            for y in range(SIZE_Y - 1, 0, -1):
                if board[y][x] not in [CHAR_EMPTY, self.char] and board[y - 1][x] == CHAR_EMPTY:
                    return x
        return super().take_turn(board)


class HeuristicAgent(Agent):
    def take_turn(self, board):
        other_players = self.other_chars(board)

        heights = board.heights()

        scores = [0] * SIZE_X
        for i in range(SIZE_X):
            if board[0][i] != CHAR_EMPTY:
                scores[i] = float('-inf')
                continue

            wls = win_lines_per_spot()[heights[i]][i]

            # add score for adjacent friendly pieces
            scores[i] += len(wls) * 8
            for y in range(max(0, heights[i] - 1), min(SIZE_Y, heights[i] + 2)):
                for x in range(max(0, i - 1), min(SIZE_X, i + 2)):
                    if board[y][x] == self.char:
                        scores[i] += 40

            # add score for direct wins
            my_board = board.copy()
            my_board.place_piece(i, self.char)
            if my_board.check_win() == self.char:
                scores[i] += 100000

            for other_char in other_players + [self.char]:
                # add score for blocking enemy triples
                triple_setup = [CHAR_EMPTY, other_char, other_char, CHAR_EMPTY]
                for line in wls:
                    matching = True
                    for j, spot in enumerate(line):
                        if board[spot[1]][spot[0]] != triple_setup[j]:
                            matching = False
                    if matching:
                        scores[i] += 200

                if heights[i] > 0:
                    # remove score for setting up enemy wins
                    my_other_board = my_board.copy()
                    my_other_board.place_piece(i, other_char)
                    if my_other_board.check_win() == other_char:
                        scores[i] -= 500

                # add score for blocking enemy wins
                other_board = board.copy()
                other_board.place_piece(i, other_char)
                if other_board.check_win() == other_char:
                    scores[i] += 500

        return argmax(scores)


class Human(Agent):
    def take_turn(self, board):
        col = int(input(f'What column do you want to play [{self.char}] on? ')) - 1
        while board[0][col] != CHAR_EMPTY:
            col = int(input(f'Column {col} already full, please choose another: '))
        return col


class Gamer(Agent):
    def take_turn(self, board):
        for i in range(1, SIZE_X):
            board.place_piece(i, self.char)
        return 0

class See3PO(Agent):
    def take_turn(self, board):

        move = self.find_move(board)
        if move == -1:
            return super().take_turn(board)
        return move
    
    def find_move(self, board):
        for col in range(SIZE_X):
            if(board[0][col] == CHAR_EMPTY):
                t_board = board.copy()
                t_board.place_piece(col, self.char)
                if t_board.check_win() != None:
                    
                    return col
            if(board[0][col] == CHAR_EMPTY):
                t_board = board.copy()
                t_board.place_piece(col, self.other_chars(board)[0])
                if t_board.check_win() != None:
                    
                    return col
        return -1


class MidLover(Agent):
    def take_turn(self, board):
        prio = [3, 2, 4, 1, 5, 0, 6]
        for col in prio:
            if board[0][col] != CHAR_EMPTY:
                return col


class SmortCenterLover(Agent):
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        for col in range(SIZE_X):
            if(board[0][col] == CHAR_EMPTY):
                    t_board = board.copy()
                    t_board.place_piece(col, self.char)
                    if t_board.check_win() != None:
                        return col

            
        for col in range(SIZE_X):
            if(board[0][col] == CHAR_EMPTY):
                t_board = board.copy()
                t_board.place_piece(col, self.other_chars(board)[0])
                if t_board.check_win() != None:
                    return col

        priority = self.createPrio()
        highestVal = 0
        highestList = []
        for i in range(SIZE_X):
            if(board[0][i] == CHAR_EMPTY):
                t_board = board.copy()
                y, x = t_board.place_piece(i, self.char)

                val = priority[y][x]
                if val > highestVal:
                    highestVal = val
                    highestList.clear()
                    highestList.append(x)
                elif val == highestVal:
                    highestList.append(x)
                
        return random.choice(highestList)

            

    def createPrio(self):
       
        x_vals = [1, 2, 3, 4, 3, 2, 1]
        y_vals = [1, 2, 3, 3, 2, 1]
        prio = [[]]
        for i in range(0, SIZE_Y):
            prio.append([])
            for j in range(0, SIZE_X):
                prio[i].append(x_vals[j] * y_vals[i])
        return prio



    def __repr__(self):
        return f'Agent({self.char})'

class Cheese(See3PO):

    def take_turn(self, board):
        if(super().find_move(board) != -1):
            return super().take_turn(board)


        if(board[5][4] == CHAR_EMPTY):
            return 4

        if(board[5][4] == self.char):
            if(board[5][3] == CHAR_EMPTY and board[5][5] == CHAR_EMPTY):
                return 3
            if(board[5][5] == CHAR_EMPTY and board[5][2] == CHAR_EMPTY):
                if(board[5][1] == CHAR_EMPTY):
                    return 2
                if(board[5][6] == CHAR_EMPTY):
                    return 5
        
        return super().take_turn(board)
