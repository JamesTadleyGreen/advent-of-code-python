from utils.grid import Grid


def check(grid: Grid, x: int, y: int, dx: int, dy: int) -> int:
    word = "".join([grid.grid[(x + dx * i, y + dy * i)] for i in range(4)])
    if word == "XMAS":
        return 1
    return 0


def check_all(grid: Grid, x: int, y: int) -> int:
    acc = 0
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        acc += check(grid, x, y, *d)
    return acc


def part1(inp: str) -> int:
    acc = 0
    grid = Grid(inp.splitlines())
    all_xs = grid.find("X")
    for x in all_xs:
        acc += check_all(grid, *x)
    return acc


def check_x(m, x, y) -> int:
    word = "".join(m.grid[(x - i, y - j)] for i in [-1, 1] for j in [-1, 1])
    if word in ["MMSS", "SSMM", "MSMS", "SMSM"]:
        return 1
    return 0


def part2(inp: str) -> int:
    acc = 0
    grid = Grid(inp.splitlines())
    all_as = grid.find("A")
    for a in all_as:
        acc += check_x(grid, *a)
    return acc
