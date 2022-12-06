# OPPONENT
# A = Rock
# B = Paper
# C = Scissors
#
# OUTCOME
# X = need to lose
# Y = need to tie
# Z = need to win
#
# My take leads to score...
# Rock;   X  1p.
# Paper;   Y 2p.
# Scissors;  Z 3p.
# 
# ADDITIONAL POINTS
# Win = 6
# Draw = 3
# Lose = 0

from dataclasses import dataclass
from typing import List

@dataclass
class RPS:
    name: str
    opponent_symbol: str
    my_symbol: str
    points: int

rock: RPS = RPS("Rock", "A", "X", 1)
paper: RPS = RPS("Paper", "B", "Y", 2)
scissors: RPS = RPS("Scissors", "C", "Z", 3)

my_symbols = {rps.my_symbol: rps for rps in [rock, paper, scissors]}
opp_symbols = {rps.opponent_symbol: rps for rps in [rock, paper, scissors]}

ADDITIONAL_POINTS_WIN: int = 6
ADDITIONAL_POINTS_TIE: int = 3
ADDITIONAL_POINTS_LOSE: int = 0

LOSE: str = 'X'
TIE: str = 'Y'
WIN: str = 'Z'

def modify_game(game: str) -> str:
    '''According to new rules in day 02_2'''
    modified_game: List[str] = list(game)
    my_play_needs_to: str = game[-1]

    if my_play_needs_to == LOSE:
        modified_game[-1] = shift_char_in_string("ABC", game[0], 2)
    elif my_play_needs_to == TIE:
        modified_game[-1] = game[0]
    else:
        modified_game[-1] = shift_char_in_string("ABC", game[0], 1)
    print(f"Modified game before shift = {modified_game}")
    # in the end, shift my chars from ABC->XYZ
    modified_game[-1] = shift_char_in_string("ABCXYZ", modified_game[-1], 3)
    return ''.join(modified_game)

def shift_char_in_string(s: str, char: str, by: int) -> str:
    '''Find char in s, then shift it "by" positions (modulo) and return the new char at the position.'''
    original_idx: int = s.index(char)
    shifted_idx: int = (original_idx + by) % len(s)
    return s[shifted_idx]

def calc_game_points(game: str) -> int:
    print(f"Modified Game = {game}")
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
            expected_points += calc_game_points(modify_game(game.rstrip()))
    print(f"Expected Points: {expected_points}")

# TEST
print("TEST RUN! Expected: 12")
day02('day02/day02_1_test.input')
# REAL
day02('day02/day02_1.input')