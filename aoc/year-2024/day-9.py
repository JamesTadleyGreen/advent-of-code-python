def parse_input(inp: str) -> list[int]:
    s = []
    value = True
    for i, v in enumerate(inp):
        if value:
            s += [int(i // 2)] * int(v)
        else:
            s += ["."] * int(v)
        value = not value
    return s


def get_value(s: list[int]) -> int:
    acc = 0
    s1 = [i for i in s if i != "."]
    for i, v in enumerate(s1):
        acc += i * v
    return acc


def part1(inp: str) -> int:
    s = parse_input(inp)
    l = len(s) - 1
    for i in range(len(s)):
        e = s[l - i]
        if e != ".":
            p = s.index(".")
            s[p] = e
            s[l - i] = "."

    return get_value(s)


def parse_input_2(inp: str) -> tuple[list[int], dict[int, tuple[int, int]]]:
    values = {}
    gaps = []
    is_gap = False
    p = 0
    for i, c in enumerate(inp):
        if is_gap:
            gaps.append((p, int(c)))
        else:
            values[i // 2] = (p, int(c))
        p += int(c)
        is_gap = not is_gap
    return gaps, values


def find_first_gap(
    value: int, gaps: list[tuple[int, int]]
) -> tuple[int, list[tuple[int, int]]]:
    for i, g in enumerate(gaps):
        if value <= g[1]:
            new_gap = (g[0] + value, g[1] - value)
            if new_gap[1] == 0:
                gaps.pop(i)
            else:
                gaps[i] = new_gap
            return g[0], gaps
    return 10000000000, []


def move_to_gap(value: tuple[int, int], gap: int) -> tuple[int, int]:
    return gap, value[1]


def pprint(values: dict[int, tuple[int, int]]):
    s = "." * 100
    for c, pos in values.items():
        s = (str(c) * pos[1]).join([s[: pos[0]], s[pos[0] + pos[1]:]])
    print(s)


def checksum(values: dict[int, tuple[int, int]]):
    acc = 0
    for c, pos in values.items():
        acc += c * sum(range(pos[0], pos[0] + pos[1]))
    return acc


def part2(inp: str) -> int:
    gaps, values = parse_input_2(inp)
    rev_values = {k: v for k, v in list(values.items())[::-1]}
    for value, pos in rev_values.items():
        first_gap, new_gaps = find_first_gap(pos[1], gaps)
        if first_gap < pos[0]:
            values[value] = move_to_gap(pos, first_gap)
            gaps = new_gaps
    return checksum(values)
