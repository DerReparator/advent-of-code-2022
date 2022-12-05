import os
import math

max_calories: int = 0

with open('day01/day01_1.input', 'r') as f:
    curr_calories: int = 0
    for line in f:
        if line.rstrip() == '':
            max_calories = max(max_calories, curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(line.rstrip())

print(f"Solution: {max_calories}")
