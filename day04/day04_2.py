from typing import List

# ...AAAAA...
# .B.........

# ...AAAAA...
# ..BB.......

# ...AAAAA...
# ..BBB......

# ...AAAAA...
# ..BBBBBBB..

def is_A_overlapping_B(a: List[int], b: List[int]) -> bool:
    return a[0] >= b[0] and a[0] <= b[1]

def parse_assignment_pair(assignment_pair: str) -> List[List[int]]:
    pair: List[List[int]] = []
    for assignment in assignment_pair.split(","):
        parsed_assignment: List[int] = []
        for idx in assignment.split('-'):
            parsed_assignment.append(int(idx))
        pair.append(parsed_assignment)
    return pair

def check_for_overlap(assignment_pair: str) -> bool:
    first_elf = parse_assignment_pair(assignment_pair)[0]
    second_elf = parse_assignment_pair(assignment_pair)[1]

    return is_A_overlapping_B(first_elf, second_elf) or is_A_overlapping_B(second_elf, first_elf)

def day04(inputFilePath: str) -> None:
    answer: int = 0
    with open(inputFilePath, 'r') as f:
        for assignment_pair in f.readlines():
            if check_for_overlap(assignment_pair.rstrip()):
                answer += 1
    print(f"Answer: {answer}")

# TEST
print("TEST RUN! Expected: 4")
day04('day04/day04_1_test.input')
# REAL
day04('day04/day04_1.input')