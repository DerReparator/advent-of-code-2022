import math
from typing import List

def char_to_priority(c: str) -> int:
    if c.isupper():
        return ord(c[0]) - (ord('A') - 27)
    else:
        return ord(c[0]) - (ord('a') - 1)

def find_badge_of_three_elves(three_rucksacks: List[str]) -> str:
    return list(set(three_rucksacks[0]) & set(three_rucksacks[1]) & set(three_rucksacks[2]))[0]

def day03(inputFilePath: str):
    priorities: int = 0
    with open(inputFilePath, 'r') as f:
        curr_three_rucksacks: List[str] = []
        for i, rucksack in enumerate(f.readlines(), start=1):
            curr_three_rucksacks.append(rucksack.rstrip())
            if i % 3 == 0:
                badge: str = find_badge_of_three_elves(curr_three_rucksacks)
                curr_three_rucksacks = [] # Reset "three rucksacks"
                priority: int = char_to_priority(badge)
                priorities += priority           
    print(f"Answer: {priorities}")

# TEST
print("TEST RUN! Expected: 70")
day03('day03/day03_1_test.input')
# REAL
day03('day03/day03_1.input')