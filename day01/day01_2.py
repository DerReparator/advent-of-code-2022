import os
import math
from typing import List

calories: List[int] = []

with open('day01/day01_1.input', 'r') as f:
    curr_calories: int = 0
    for line in f:
        if line.rstrip() == '':
            calories.append(curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(line.rstrip())

calories.sort(reverse=True)
top3_sum: int = sum(calories[:3])
print(f"Solution: {top3_sum}")
