def parse_input(input: str) -> tuple[list[int], list[int]]:
    ls: list[list[int]] = [[int(j) for j in i.split()]
                           for i in input.split("\n")]
    return zip(*ls)  # type: ignore , looks like zip isn't typechecked


def part1(input: str) -> int:
    acc = 0
    left, right = parse_input(input)
    left = sorted(left)
    right = sorted(right)
    for i in range(len(left)):
        acc += abs(left[i] - right[i])
    return acc


def part2(input: str) -> int:
    acc = 0
    left, right = parse_input(input)
    for i in left:
        acc += i * right.count(i)
    return acc
