# OPPONENT
# A = Rock
# B = Paper
# C = Scissors
#
# MYSELF
# X = Rock;     1p.
# Y = Paper;    2p.
# Z = Scissors; 3p.
# 
# ADDITIONAL POINTS
# Win = 6
# Draw = 3
# Lose = 0

from dataclasses import dataclass

@dataclass
class RPS:
    name: str
    opponent_symbol: str
    myself_symbol: str
    points: int

rock: RPS = RPS("Rock", "A", "X", 1)
paper: RPS = RPS("Paper", "B", "Y", 2)
scissors: RPS = RPS("Scissors", "C", "Z", 3)

my_symbols = {rps.myself_symbol: rps for rps in [rock, paper, scissors]}
opp_symbols = {rps.opponent_symbol: rps for rps in [rock, paper, scissors]}

ADDITIONAL_POINTS_WIN: int = 6
ADDITIONAL_POINTS_TIE: int = 3
ADDITIONAL_POINTS_LOSE: int = 0

def calc_game_points(game: str) -> int:
    opp_symbol: str = game[0]
    my_symbol: str = game[-1]

    opp_rps: RPS = opp_symbols[opp_symbol]
    my_rps: RPS = my_symbols[my_symbol]

    game_points: int = 0

    if opp_rps.name == my_rps.name:
        game_points += ADDITIONAL_POINTS_TIE
    elif my_rps.points - opp_rps.points in (1, -2):
        game_points += ADDITIONAL_POINTS_WIN

    return my_rps.points + game_points

def day02(inputFilePath: str):
    expected_points: int = 0
    with open(inputFilePath, 'r') as f:
        for game in f.readlines():
            expected_points += calc_game_points(game.rstrip())
    print(f"Expected Points: {expected_points}")

# TEST
print("TEST RUN! Expected: 15")
day02('day02/day02_1_test.input')
# REAL
day02('day02/day02_1.input')