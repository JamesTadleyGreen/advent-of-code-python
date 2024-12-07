from itertools import product


def parse_line(line):
    answer, factors = line.split(": ")
    return int(answer), [int(i) for i in factors.split()]


def part1(inp: str) -> int:
    acc = 0
    for line in inp.splitlines():
        answer, factors = parse_line(line)
        acc += check_line(answer, factors)
    return acc


def check_line(answer, factors):
    for combo in product([True, False], repeat=len(factors)):
        acc = factors[0]
        for f, c in zip(factors[1:], combo):
            if c:
                acc *= f
            else:
                acc += f
        if acc == answer:
            return answer
    return 0


def part2(inp: str) -> int:
    acc = 0
    for line in inp.splitlines():
        answer, factors = parse_line(line)
        acc += check_line_with_conact(answer, factors)
    return acc


def check_line_with_conact(answer, factors):
    for combo in product([0, 1, 2], repeat=len(factors)):
        acc = factors[0]
        for f, c in zip(factors[1:], combo):
            if c == 0:
                acc *= f
            elif c == 1:
                acc += f
            else:
                acc = int(str(acc) + str(f))
        if acc == answer:
            return answer
    return 0
