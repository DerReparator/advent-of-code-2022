import math

def char_to_priority(c: str) -> int:
    if c.isupper():
        return ord(c[0]) - (ord('A') - 27)
    else:
        return ord(c[0]) - (ord('a') - 1)

def find_wrong_packed_item(rucksack: str) -> str:
    half_the_size: int = math.floor(len(rucksack)/2)
    first_compartment = set(rucksack[:half_the_size])
    second_compartment = set(rucksack[half_the_size:])

    for item in first_compartment:
        if item in second_compartment:
            return item

def day03(inputFilePath: str):
    priorities: int = 0
    with open(inputFilePath, 'r') as f:
        for rucksack in f.readlines():
            wrong_packed_item: str = find_wrong_packed_item(rucksack)
            priority: int = char_to_priority(wrong_packed_item)
            priorities += priority
    print(f"Answer: {priorities}")

# TEST
print("TEST RUN! Expected: 157")
day03('day03/day03_1_test.input')
# REAL
day03('day03/day03_1.input')