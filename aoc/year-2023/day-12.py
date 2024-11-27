def parse_key(key: str) -> list[int]:
    return [int(i) for i in key.split(',')]

def completed_puzzle_check(puzzle, key)-> int:
    result = [len(i) for i in puzzle.split('.') if i != '']
    if result == key:
        return 1
    return 0

def get_arrangements(puzzle, key):
    if not ('?' in puzzle):
        return completed_puzzle_check(puzzle, key)
    return get_arrangements(puzzle.replace('?', '.', 1), key) + get_arrangements(puzzle.replace('?', '#', 1), key)

def part1(input: str) -> int:
    arrangements = 0
    for line in input.split('\n'):
        puzzle, key = line.split(' ')
        arrangements += get_arrangements(puzzle, parse_key(key))
    return arrangements
