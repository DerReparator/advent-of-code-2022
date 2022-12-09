MARKER_NO_OF_DISTINCT_SYMBOLS: int = 14

def is_packet_marker(four_chars: str) -> bool:
    return len(set(four_chars)) is len(four_chars)

def search_for_packet_marker(stream: str) -> int:
    for i in range(MARKER_NO_OF_DISTINCT_SYMBOLS, len(stream)):
        if is_packet_marker(stream[i-MARKER_NO_OF_DISTINCT_SYMBOLS:i]):
            return i

def day06(inputFilePath: str) -> None:
    with open(inputFilePath, 'r') as f:
        for signal in f.readlines():
            idx: int = search_for_packet_marker(signal)
            print(f"Answer: {idx}")

# TEST
#print("TEST RUN! Expected:\t19\t23\t23\t29\t26")
#day06('day06/day06_1_test.input')
# REAL
day06('day06/day06_1.input')