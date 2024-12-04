from collections import defaultdict
from collections.abc import Iterator
from typing import TypeVar, Generic

T = TypeVar("T", int, str)


class Grid(Generic[T]):
    def __init__(self, grid: list[list[T]], default: T | None = None):
        d = defaultdict(type(grid[0][0]))
        for y, line in enumerate(grid):
            for x, value in enumerate(line):
                d[(x, y)] = value
        if default is not None:
            assert default is not None
            d.default_factory = lambda: default
        self.grid = d
        self.dimensions = (len(grid[0]), len(grid))

    def find(self, value: T) -> list[T]:
        output = []
        for k, v in self.grid.items():
            if v == value:
                output.append(k)
        return output
