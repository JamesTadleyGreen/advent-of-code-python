from utils.grid import Grid

import numpy as np


def parse_input(inp: str) -> Grid:
    return Grid(inp)


def get_neighbours(limit: int, position: tuple[int, int]):
    all_neighbours = [
        position + np.array(i) for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ]
    return [
        tuple(neighbour)
        for neighbour in all_neighbours
        if 0 <= neighbour[0] < limit and 0 <= neighbour[1] < limit
    ]


def parse_route(track: Grid) -> list[tuple[int, int]]:
    start = track.find("S")[0]
    end = track.find("E")[0]
    limit = track.grid.shape[0]
    output = [start]
    current = start
    while end not in (neighbours := get_neighbours(limit, current)):
        for neighbour in neighbours:
            if track.grid[neighbour] == ".":
                if neighbour not in output:
                    output.append(neighbour)
                    current = neighbour
    return output + [end]


def taxicab_metric(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part1(inp: str) -> int:
    track = parse_input(inp)
    positions = parse_route(track)
    acc = 0
    time_save = 100
    for i, position in enumerate(positions[:-time_save]):
        for shortcut in positions[i + time_save + 1:]:
            if taxicab_metric(position, shortcut) <= 2:
                acc += 1
    return acc


def part2(inp: str) -> int:
    track = parse_input(inp)
    positions = parse_route(track)
    acc = 0
    min_time_save = 100
    for i, position in enumerate(positions[:-min_time_save]):
        for j, shortcut in enumerate(positions[i + min_time_save:]):
            distance = taxicab_metric(position, shortcut)
            time_save = min_time_save + j - distance
            if distance <= 20 and time_save >= min_time_save:
                acc += 1
    return acc
