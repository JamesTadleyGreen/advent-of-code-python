from typing import Optional
from utils.grid import Grid
import numpy as np


def parse_input(inp: str) -> tuple[Grid, np.array, list[np.array]]:
    map_string, instruction_string = inp.split("\n\n")
    instructions = []
    for i in instruction_string:
        if i == "v":
            instructions.append(np.array((1, 0)))
        if i == "<":
            instructions.append(np.array((0, -1)))
        if i == ">":
            instructions.append(np.array((0, 1)))
        if i == "^":
            instructions.append(np.array((-1, 0)))
    map = Grid(map_string)
    robot = map.find("@")[0]
    map.grid[tuple(robot)] = "."
    return map, robot, instructions


def first_space(
    map: Grid, robot: np.array, instruction: np.array
) -> Optional[np.array]:
    pos = robot + instruction
    i = 1
    while min(pos) > 0 and all(pos < map.grid.shape):
        if map.grid[tuple(pos)] == ".":
            return pos
        if map.grid[tuple(pos)] == "#":
            return None
        i += 1
        pos += instruction
    return None


def move(map: Grid, robot: np.array, instruction: np.array) -> tuple[Grid, np.array]:
    new_pos = robot + instruction
    if map.grid[tuple(new_pos)] == "#":
        return map, robot
    if map.grid[tuple(new_pos)] == ".":
        return map, new_pos
    space = first_space(map, new_pos, instruction)
    if space is None:
        return map, robot
    map.grid[tuple(new_pos)] = "."
    map.grid[tuple(space)] = "O"
    return map, new_pos


def gps(map: Grid) -> int:
    acc = 0
    boxes = map.find("O")
    for box in boxes:
        acc += box[1] * 100 + box[0]
    return acc


def part1(inp: str) -> int:
    map, robot, instructions = parse_input(inp)
    for instruction in instructions:
        map, robot = move(map, robot, instruction)
    return gps(map)


def resize_map(map: Grid) -> Grid:
    return Grid(
        "\n".join(
            ["".join([("[]" if i == "O" else i * 2) for i in row])
             for row in map.grid]
        )
    )


def top(
    map: Grid, boxes: list[np.array], instruction: np.array
) -> Optional[set[tuple[np.array, np.array]]]:
    output = set()
    for box in boxes:
        for box_part in box:
            next = box_part + instruction
            value = map.grid[tuple(next)]
            if value == "#":
                return None
            if value == "[":
                output.add((tuple(next), tuple(next + np.array((0, 1)))))
            if value == "]":
                output.add((tuple(next + np.array((0, -1))), tuple(next)))
    return output


def find_boxes(map: Grid, robot: np.array, instruction: np.array) -> list[np.array]:
    if instruction[0] == 0:
        space = first_space(map, robot, instruction)
        if space is None:
            return []
        if instruction[1] == 1:
            return [
                (robot + instruction * i, robot + instruction * (i + 1))
                for i in range(0, abs(space[1] - robot[1]), 2)
            ]
        else:
            return [
                (robot + instruction * (i + 1), robot + instruction * i)
                for i in range(0, abs(space[1] - robot[1]), 2)
            ]
    boxes = []
    if map.grid[tuple(robot)] == "[":
        current_boxes = [(robot, robot + np.array((0, 1)))]
    else:
        current_boxes = [(robot + np.array((0, -1)), robot)]
    while True:
        next_boxes = top(map, current_boxes, instruction)
        if next_boxes is None:
            return []
        boxes += current_boxes
        current_boxes = next_boxes
        if next_boxes == set():
            return boxes


def move_boxes(map: Grid, boxes: list[np.array], instruction: np.array) -> Grid:
    for box in boxes:
        left, right = box
        map.grid[tuple(left)] = "."
        map.grid[tuple(right)] = "."
    for box in boxes:
        left, right = box
        map.grid[tuple(left + instruction)] = "["
        map.grid[tuple(right + instruction)] = "]"
    return map


def move_2(map: Grid, robot: np.array, instruction: np.array) -> tuple[Grid, np.array]:
    new_pos = robot + instruction
    if map.grid[tuple(new_pos)] == "#":
        return map, robot
    if map.grid[tuple(new_pos)] == ".":
        return map, new_pos
    boxes = find_boxes(map, new_pos, instruction)
    if boxes == []:
        return map, robot
    map = move_boxes(map, boxes, instruction)
    return map, new_pos


def gps_2(map: Grid) -> int:
    acc = 0
    boxes = map.find("[")
    for box in boxes:
        acc += box[0] * 100 + box[1]
    return acc


def part2(inp: str) -> int:
    map, robot, instructions = parse_input(inp)
    map = resize_map(map)
    robot = (robot[0], robot[1] * 2)
    for instruction in instructions:
        map, robot = move_2(map, robot, instruction)
    return gps_2(map)
