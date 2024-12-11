from collections import defaultdict
from functools import cache


def parse_input(inp: str) -> defaultdict[int, int]:
    d = defaultdict(int)
    for stone in inp.split():
        d[int(stone)] += 1
    return d


@cache
def next(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    stone_str = str(stone)
    length = len(stone_str)
    if length % 2 == 0:
        return [int(stone_str[: length // 2]), int(stone_str[length // 2:])]
    return [stone * 2024]


def blink(stones: defaultdict[int, int]) -> defaultdict[int, int]:
    d = defaultdict(int)
    for stone, value in stones.items():
        for next_stone in next(stone):
            d[next_stone] += value
    return d


def part1(inp: str) -> int:
    stones = parse_input(inp)
    for _ in range(25):
        stones = blink(stones)
    return sum(stones.values())


def part2(inp: str) -> int:
    stones = parse_input(inp)
    for _ in range(75):
        stones = blink(stones)
    return sum(stones.values())
