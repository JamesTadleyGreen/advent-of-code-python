import numpy as np


def parse_command(command: str) -> tuple[str, tuple[int, int], tuple[int, int]]:
    words = command.split(" through ")
    end = words[-1]
    *action, start = words[0].split(" ")
    action = " ".join(action).strip()
    sx, sy = start.split(",")
    ex, ey = end.split(",")
    return action, (int(sx), int(sy)), (int(ex), int(ey))


def modify_bits(
    array: np.array, start: tuple[int, int], end: tuple[int, int], value: bool
) -> np.array:
    sx, sy = start
    ex, ey = end
    array[sx : ex + 1, sy : ey + 1] = value
    return array


def toggle_bits(
    array: np.array, start: tuple[int, int], end: tuple[int, int]
) -> np.array:
    sx, sy = start
    ex, ey = end
    array[sx : ex + 1, sy : ey + 1] = ~array[sx : ex + 1, sy : ey + 1]
    return array


def part1(input: str) -> int:
    array = np.zeros((1000, 1000), dtype=bool)
    for command in input.split("\n"):
        action, start, end = parse_command(command)
        if action == "turn on":
            modify_bits(array, start, end, True)
        if action == "turn off":
            modify_bits(array, start, end, False)
        if action == "toggle":
            toggle_bits(array, start, end)
    return np.sum(array)


def modify_bits_v2(
    array: np.array, start: tuple[int, int], end: tuple[int, int], value: int
) -> np.array:
    sx, sy = start
    ex, ey = end
    array[sx : ex + 1, sy : ey + 1] += value
    return min_zero(array)


def min_zero(array: np.array) -> np.array:
    array[array < 0] = 0
    return array


def part2(input: str) -> int:
    array = np.zeros((1000, 1000), dtype=int)
    for command in input.split("\n"):
        action, start, end = parse_command(command)
        if action == "turn on":
            modify_bits_v2(array, start, end, 1)
        if action == "turn off":
            modify_bits_v2(array, start, end, -1)
        if action == "toggle":
            modify_bits_v2(array, start, end, 2)
    return np.sum(array)
