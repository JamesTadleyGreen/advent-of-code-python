import numpy as np
import math


def parse_input(inp: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    output = []
    for line in inp.splitlines():
        pos, vel = line.split(" ")
        pos = np.array(list(map(int, pos[2:].split(","))))
        vel = np.array(list(map(int, vel[2:].split(","))))
        output.append((pos, vel))
    return output


def get_position(
    robot: tuple[np.array, np.array], dimensions: tuple[int, int], seconds: int
) -> tuple[int, int]:
    dim_x, dim_y = dimensions
    pos, vel = robot
    final_pos = pos + vel * seconds
    return np.array([final_pos[0] % dim_x, final_pos[1] % dim_y])


def get_positions(
    robots: list[tuple[np.array, np.array]], dimensions: tuple[int, int], seconds: int
):
    return [get_position(robot, dimensions, seconds) for robot in robots]


def saftey_factor(positions: list[np.array], dimensions: tuple[int, int]) -> int:
    quadrents = [0, 0, 0, 0]
    for position in positions:
        if position[0] < dimensions[0] // 2:
            if position[1] < dimensions[1] // 2:
                quadrents[0] += 1
            if position[1] > dimensions[1] // 2:
                quadrents[1] += 1
        if position[0] > dimensions[0] // 2:
            if position[1] < dimensions[1] // 2:
                quadrents[2] += 1
            if position[1] > dimensions[1] // 2:
                quadrents[3] += 1
    return math.prod(quadrents)


def part1(inp: str) -> int:
    robots = parse_input(inp)
    dimensions = (101, 103)
    positions = get_positions(robots, dimensions, seconds=100)
    return saftey_factor(positions, dimensions)


def closeness(positions: list[np.array]) -> int:
    average = sum(positions) / len(positions)
    linear_distance = sum([(position - average) ** 2 for position in positions])
    return sum(linear_distance)


def show_positions(
    positions: list[tuple[int, int]], dimensions: tuple[int, int]
) -> str:
    dim_x, dim_y = dimensions
    grid = [["." for _ in range(dim_x)] for _ in range(dim_y)]
    for pos in positions:
        grid[pos[1]][pos[0]] = "#"
    return "\n".join("".join(row) for row in grid)


def part2(inp: str) -> int:
    robots = parse_input(inp)
    dimensions = (101, 103)
    i = 0
    stop = False
    distance = 1000000000000
    while not stop:
        positions = get_positions(robots, dimensions, seconds=i)
        if (new_distance := closeness(positions)) < distance:
            print(show_positions(positions, dimensions))
            distance = new_distance
            tree = input(f"Christmas Tree at {i} seconds?")
            if tree != "":
                stop = True
        i += 1
    return i
