import re
import math
import numpy as np


def parse_input(inp: str) -> list[tuple[np.array, np.array]]:
    output = []
    numbers = [int(i) for i in re.findall(r"(\d+)", inp)]
    for i in range(0, len(numbers), 6):
        a = numbers[i], numbers[i + 2]
        b = numbers[i + 1], numbers[i + 3]
        target = numbers[i + 4], numbers[i + 5]
        output.append((np.array([a, b]), np.array(target)))
    return output


def calculate_tokens(target: np.array, buttons: np.array) -> np.array:
    buttons_inv = np.linalg.inv(buttons)
    button_presses = np.matmul(buttons_inv, target)
    tickets = np.matmul([3, 1], button_presses)
    if all(map(lambda x: math.isclose(x - round(x), 0, abs_tol=0.001), button_presses)):
        return round(tickets)
    return 0


def part1(inp: str) -> int:
    machines = parse_input(inp)
    tokens = 0
    for machine in machines:
        buttons, target = machine
        tokens += calculate_tokens(target, buttons)
    return tokens


def part2(inp: str) -> int:
    machines = parse_input(inp)
    tokens = 0
    for i, machine in enumerate(machines):
        buttons, target = machine
        tokens += calculate_tokens(target + 10_000_000_000_000, buttons)
    return tokens
