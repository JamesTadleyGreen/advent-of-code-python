from functools import cache
import re

INSTRUCTIONS = ["AND", "OR", "LSHIFT", "RSHIFT"]
SIGNALS = {}


def get_operation(instruction: str) -> tuple[str, ...]:
    words = instruction.split(" ")
    for word in INSTRUCTIONS:
        if word in instruction:
            return word, words[0], words[2], words[4]
    if "NOT" in instruction:
        return "NOT", words[1], words[3]
    return "WIRE", words[0], words[2]


def part1(input: str) -> int:
    for instruction in input.split("\n"):
        operation, *args, to = get_operation(instruction)
        SIGNALS[to] = (operation, args)
    value = parse_signals("a")
    if value < 0:
        value += 65536
    return value


def part2(input: str) -> int:
    new_b = part1(input)
    print(input.__repr__())
    input = re.sub(r"\n19138 -> b", f"\n{new_b} -> b", input)
    return part1(input)


@cache
def get(signal: str) -> int:
    if signal.isdigit():
        return int(signal)
    return parse_signals(signal)


def parse_signals(start: str) -> int:
    if isinstance(SIGNALS[start], int):
        return SIGNALS[start]
    operation, args = SIGNALS[start]
    if operation == "WIRE":
        return get(args[0])
    elif operation == "NOT":
        return ~get(args[0])
    elif operation == "AND":
        first, second = args
        return get(first) & get(second)
    elif operation == "OR":
        first, second = args
        return get(first) | get(second)
    elif operation == "LSHIFT":
        first, count = args
        return get(first) << get(count)
    elif operation == "RSHIFT":
        first, count = args
        return get(first) >> get(count)
    raise Exception
