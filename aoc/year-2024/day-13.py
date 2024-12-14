import re


def parse_input(inp: str) -> list[tuple[int, int, int]]:
    output = []
    for block in inp.split("\n\n"):
        a, b, target = block.split("\n")
        a_s = re.search(r"X\+(\d+), Y\+(\d+)", a)
        b_s = re.search(r"X\+(\d+), Y\+(\d+)", b)
        target_s = re.search(r"X=(\d+), Y=(\d+)", target)
        output.append(
            (
                (int(a_s.group(1)), int(a_s.group(2))),
                (int(b_s.group(1)), int(b_s.group(2))),
                (int(target_s.group(1)), int(target_s.group(2))),
            )
        )
    return output


def calculate_tokens(target, b, a):
    tokens = 0
    while target[0] > 0 and target[1] > 0:
        if target[0] % a[0] == 0:
            remaining_tokens = target[0] // a[0]
            if target[1] - a[1] * remaining_tokens == 0:
                print(tokens, remaining_tokens)
                return tokens + remaining_tokens
        target = (target[0] - b[0], target[1] - b[1])
        tokens += 3
    return 0


def part1(inp: str) -> int:
    machines = parse_input(inp)
    tokens = 0
    for machine in machines:
        a, b, target = machine
        print(target)
        tokens += calculate_tokens(target, a, b)
        print(tokens)
    return tokens
