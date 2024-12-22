from collections import defaultdict
from functools import cache


def parse_input(inp: str) -> list[int]:
    return [int(i) for i in inp.splitlines()]


def mix(a: int, b: int) -> int:
    return a ^ b


def prune(a: int) -> int:
    return a % 16777216


def get_pseudorandom(secret: int, iterations: int) -> int:
    for _ in range(iterations):
        secret = get_next_pesudorandom(secret)
    return secret


@cache
def get_next_pesudorandom(secret: int) -> int:
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def part1(inp: str) -> int:
    acc = 0
    secrets = parse_input(inp)
    for secret in secrets:
        acc += get_pseudorandom(secret, 2000)
    return acc


def generate_pseudorandom(secret: int, iterations: int) -> list[int]:
    output = [secret]
    for _ in range(iterations):
        secret = get_next_pesudorandom(secret)
        output.append(secret)
    return output


def add_sequences(secret: int):
    output = {}
    sequence = [i % 10 for i in generate_pseudorandom(secret, 2000)]
    differences = []
    for i in range(1, len(sequence)):
        differences.append(sequence[i] - sequence[i - 1])
    for i in range(3, len(differences)):
        seq = (
            differences[i - 3],
            differences[i - 2],
            differences[i - 1],
            differences[i],
        )
        if seq not in output:
            output[seq] = sequence[i + 1]
    return output


def part2(inp: str) -> int:
    secrets = parse_input(inp)
    instructions = defaultdict(int)
    for secret in secrets:
        d = add_sequences(secret)
        for k, v in d.items():
            instructions[k] += v
    return max(instructions.values())
