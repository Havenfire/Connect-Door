import cProfile
import connect_4
from constants import *

pr = cProfile.Profile()

wins = {None: 0, CHAR_0: 0, CHAR_1: 0}

pr.enable()

for _ in range(100):
    board = connect_4.initialize()
    winner = connect_4.main_loop(board)
    wins[winner] += 1


pr.disable()
pr.dump_stats('tmp/profile.prof')


print(wins)
