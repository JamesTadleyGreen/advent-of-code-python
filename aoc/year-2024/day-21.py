KEYPAD = {
    " ": (0, 3),
    "A": (2, 3),
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
}

DIRECTIONAL_KEYPAD = {
    " ": (0, 0),
    "A": (2, 0),
    "^": (1, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def get_path(
    start: tuple[int, int], end: tuple[int, int], blank: tuple[int, int]
) -> str:
    if start[1] < end[1]:
        if start[0] < end[0]:
            pattern = "v" * abs(start[1] - end[1]) + ">" * abs(start[0] - end[0])
        else:
            pattern = "<" * abs(start[0] - end[0]) + "v" * abs(start[1] - end[1])
    elif start[0] > end[0]:
        pattern = "^" * abs(start[1] - end[1]) + "<" * abs(start[0] - end[0])
    else:
        pattern = ">" * abs(start[0] - end[0]) + "^" * abs(start[1] - end[1])
    if start[0] <= blank[0] <= end[0] and start[1] <= blank[1] <= end[1]:
        pattern = pattern.split()
        pattern[-1], pattern[-2] = pattern[-2], pattern[-1]
        return "".join(pattern)
    return pattern


def reverse(instructions: str, keypad: dict) -> str:
    output = ""
    current = keypad["A"]
    for c in instructions:
        if c == ">":
            current = current[0] + 1, current[1]
        elif c == "<":
            current = current[0] - 1, current[1]
        elif c == "v":
            current = current[0], current[1] + 1
        elif c == "^":
            current = current[0], current[1] - 1
        else:  # A
            output += [k for k, v in keypad.items() if v == current][0]
    return output


def keypad_to_directional(code: str) -> str:
    output = ""
    current = "A"
    while code != "":
        first = code[0]
        output += get_path(KEYPAD[current], KEYPAD[first], KEYPAD[" "])
        output += "A"
        current = first
        code = code[1:]
    print(output)
    return output


def directional_to_directional(code: str) -> str:
    output = ""
    current = "A"
    while code != "":
        first = code[0]
        output += get_path(
            DIRECTIONAL_KEYPAD[current],
            DIRECTIONAL_KEYPAD[first],
            DIRECTIONAL_KEYPAD[" "],
        )
        output += "A"
        current = first
        code = code[1:]
    print(output)
    return output


def shortest_presses(code: str) -> str:
    return directional_to_directional(
        directional_to_directional(keypad_to_directional(code))
    )


def part1(inp: str) -> int:
    acc = 0
    codes = inp.splitlines()
    tmp = "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    print(tmp)
    print(
        reverse(
            tmp,
            DIRECTIONAL_KEYPAD,
        )
    )
    print(reverse(reverse(tmp, DIRECTIONAL_KEYPAD), DIRECTIONAL_KEYPAD))
    print(
        reverse(reverse(reverse(tmp, DIRECTIONAL_KEYPAD), DIRECTIONAL_KEYPAD), KEYPAD)
    )
    for code in codes:
        print(code, shortest_presses(code), len(shortest_presses(code)))
        acc += len(shortest_presses(code)) * int(code[:-1])
    return acc
