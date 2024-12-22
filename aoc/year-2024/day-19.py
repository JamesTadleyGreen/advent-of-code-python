from functools import cache


def parse_input(inp: str) -> tuple[tuple, list[str]]:
    towels, designs = inp.split("\n\n")
    return tuple(towels.split(", ")), designs.splitlines()


@cache
def possible(towels: tuple, design: str) -> bool:
    if design == "":
        return True
    possible_towels = [towel for towel in towels if design.startswith(towel)]
    if possible_towels == []:
        return False
    return any(possible(towels, design[len(towel):]) for towel in possible_towels)


@cache
def number_of_combinations(towels: tuple, design: str) -> int:
    if design == "":
        return 1
    possible_towels = [towel for towel in towels if design.startswith(towel)]
    if possible_towels == []:
        return 0
    return sum(
        number_of_combinations(towels, design[len(towel):])
        for towel in possible_towels
    )


def part1(inp: str) -> int:
    acc = 0
    towels, designs = parse_input(inp)
    for design in designs:
        acc += possible(towels, design)
    return acc


def part2(inp: str) -> int:
    acc = 0
    towels, designs = parse_input(inp)
    for design in designs:
        number = number_of_combinations(towels, design)
        acc += number
    return acc
