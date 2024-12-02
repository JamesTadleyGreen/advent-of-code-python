def is_increasing(ls: list[int]) -> bool:
    for i in range(1, len(ls)):
        if ls[i] < ls[i - 1]:
            return False
    return True


def is_monotone(ls: list[int]) -> bool:
    return is_increasing(ls) or is_increasing(ls[::-1])


def bounded(ls: list[int]) -> bool:
    for i in range(1, len(ls)):
        if abs(ls[i - 1] - ls[i]) > 3 or abs(ls[i - 1] - ls[i]) < 1:
            return False
    return True


def part1(input: str) -> int:
    acc = 0
    for line in input.splitlines():
        parsed_line = [int(i) for i in line.split()]
        if is_monotone(parsed_line) and bounded(parsed_line):
            acc += 1
    return acc


def part2(input: str) -> int:
    acc = 0
    for line in input.splitlines():
        parsed_line = [int(i) for i in line.split()]
        for i in range(len(parsed_line)):
            permutation = (
                parsed_line[:i] + parsed_line[i + 1:]
            )  # There's a smarter way of doing this I think
            if is_monotone(permutation) and bounded(permutation):
                acc += 1
                break
    return acc
