from typing import List
from dataclasses import dataclass

@dataclass
class Move:
    amount: int
    from_idx: int
    to_idx: int

def parse_stacks(starting_stacks: List[str]) -> List[List[str]]:
    stacks: List[List[str]] = []
    # Setup stacks
    for _ in range(1, len(starting_stacks[0]), 4):
        stacks.append([])
    print(f"DEBUG number of stacks={len(stacks)}")
    # parse the input onto the stacks
    for line in starting_stacks:
        for i in range(1, len(line), 4):
            c = line[i]
            stack_idx = int((i - 1) / 4)
            if c.isdigit():
                break
            if c.isupper():
                stacks[stack_idx].append(c)
        else:
            continue
        break
    # Flip the stack because we parsed from top to bottom
    for stack in stacks:
        stack.reverse()
    return stacks


def parse_moves(starting_stacks: List[str]) -> List[Move]:
    moves: List[Move] = []
    for line in starting_stacks:
        if line[0] == 'm':
            splitted_line = line.split(' ')
            moves.append(Move(int(splitted_line[1]), int(splitted_line[3]), int(splitted_line[5].rstrip())))
    return moves

def execute_crane(stacks: List[List[str]], moves: List[Move]) -> None:
    for move in moves:
        for _ in range(move.amount):
            stacks[move.to_idx - 1].append(stacks[move.from_idx - 1].pop())

def day05(inputFilePath: str) -> None:
    answer: str = ""
    starting_stacks: List[str]
    with open(inputFilePath, 'r') as f:
        starting_stacks = f.readlines()
    stacks: List[List[str]] = parse_stacks(starting_stacks)
    print(f"DEBUG stacks: {stacks}")
    moves: List[Move] = parse_moves(starting_stacks)
    print(f"DEBUG moves: {moves}")
    execute_crane(stacks, moves)
    answer = "".join([stack.pop() for stack in stacks])
    print(f"Answer: {answer}")

# TEST
print("TEST RUN! Expected: 'CMZ'")
#day05('day05/day05_1_test.input')
# REAL
day05('day05/day05_1.input')