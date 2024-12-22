import numpy as np
from typing import TypeVar, Generic

T = TypeVar("T", int, str)


class Grid(Generic[T]):
    def __init__(self, data: str):
        self.grid = np.array([[j for j in i] for i in data.splitlines()])
        self.dimensions = self.grid.shape

    def find(self, value: T) -> list[T]:
        all_loc = np.where(self.grid == value)
        return [(all_loc[0][i], all_loc[1][i]) for i in range(len(all_loc[0]))]

    def pad(self, pad_with, value):
        self.grid = np.pad(self.grid, pad_with, "constant",
                           constant_values=value)
