import re


def part1(input: str) -> int:
    acc = 0
    matches = re.findall("mul\(\d+,\d+\)", input)
    for group in matches:
        first, last = group[4:-1].split(",")
        acc += int(first) * int(last)
    return acc


def part2(inp: str) -> int:
    acc = 0
    p = [[j for j in i.split("do()")[1:]] for i in inp.split("don't()")]
    for j in p:
        acc += part1("".join(j))
    return acc
