def check(m, x, y, x1, y1) -> int:
    try:
        if ((y + y1 * 3) < 0) or ((x + x1 * 3) < 0):
            return 0
        word = [m[y + y1 * i][x + x1 * i] for i in range(4)]
        if "".join(word) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0


def check_all(m, x, y) -> int:
    acc = 0
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        acc += check(m, x, y, *d)
    return acc


def part1(inp: str) -> int:
    acc = 0
    m = inp.splitlines()
    for y in range(len(m)):
        for x in range(len(m[0])):
            acc += check_all(m, x, y)
    return acc


def check_x(m, x, y) -> int:
    if x == 0 or y == 0:
        return 0
    try:
        word = (
            m[y][x]
            + m[y - 1][x - 1]
            + m[y + 1][x - 1]
            + m[y - 1][x + 1]
            + m[y + 1][x + 1]
        )
        if word in ["AMMSS", "ASSMM", "ASMSM", "AMSMS"]:
            return 1
        return 0
    except IndexError:
        return 0


def part2(inp: str) -> int:
    acc = 0
    m = inp.splitlines()
    for y in range(len(m)):
        for x in range(len(m[0])):
            acc += check_x(m, x, y)
    return acc
