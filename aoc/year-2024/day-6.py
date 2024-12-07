from utils.grid import Grid
import numpy as np


def next_direction(d: tuple[int, int]):
    if d[0] == 0:
        return -d[1], 0
    return 0, d[0]


def is_infront(pos, obstacle, direction):
    if direction > 0:
        return pos > obstacle
    return pos < obstacle


def get_edge(pos: int, direction: int, grid_size: int):
    if direction == -1:
        return pos
    return grid_size - pos - 1


def get_next_pos(
    pos: tuple[int, int],
    direction: tuple[int, int],
    obstacles: list[tuple[int, int]],
    grid_size: int,
):
    index = 0 if direction[0] != 0 else 1
    possible_obstacles = [
        i
        for i in obstacles
        if pos[1 - index] == i[1 - index]
        and not is_infront(pos[index], i[index], direction[index])
    ]
    if possible_obstacles == []:
        return (
            None,
            (0, 0),
            {
                tuple(np.add(pos, np.multiply(direction, i)))
                for i in range(get_edge(pos[index], direction[index], grid_size) + 1)
            },
        )
    obstacle = min(possible_obstacles, key=lambda x: abs(x[index] - pos[index]))
    final_pos = np.subtract(obstacle, direction)
    distance = np.max(np.abs(np.subtract(obstacle, pos)))
    visited = {tuple(np.add(pos, np.multiply(direction, i))) for i in range(distance)}
    return final_pos, next_direction(direction), visited


def get_distinct_positions(
    start: tuple[int, int], obstacles: list[tuple[int, int]], grid_size: int
):
    pos = start
    direction = (0, -1)
    all_visited = {pos}
    while pos is not None:
        pos, direction, visited = get_next_pos(pos, direction, obstacles, grid_size)
        all_visited |= visited
    return all_visited


def part1(inp: str) -> int:
    grid = Grid(inp)
    grid_size = grid.dimensions[0]
    all_obstacles = grid.find("#")
    start = grid.find("^")[0]
    return len(get_distinct_positions(start, all_obstacles, grid_size))


def is_loop(start: tuple[int, int], obstacles: list[tuple[int, int]]):
    pos = start
    direction = (0, -1)
    seen = {(start, direction)}
    while pos is not None:
        pos, direction, _ = get_next_pos(pos, direction, obstacles, 0)
        if pos is None:
            return False
        new_loc = (tuple(pos), direction)
        if new_loc in seen:
            return True
        seen.add(new_loc)


def part2(inp: str) -> int:
    acc = 0
    grid = Grid(inp)
    all_obstacles = grid.find("#")
    start = grid.find("^")[0]
    potential_placements = get_distinct_positions(
        start, all_obstacles, grid.dimensions[0]
    )
    for p in potential_placements:
        if is_loop(start, all_obstacles + [p]):
            acc += 1
    return acc
