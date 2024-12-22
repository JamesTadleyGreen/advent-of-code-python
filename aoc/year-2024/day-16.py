from utils.graph import Graph
from utils.grid import Grid


def min_score(graph: Graph, start: tuple[int, int]) -> int:
    pass


def parse_input(inp: str) -> tuple[Graph, tuple[int, int]]:
    grid = Grid(inp)
    start = (1, len(inp.splitlines))
    graph = Graph()


def get_neighbours(grid: np.array, node: np.array):
    current = start
    for dir in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        next = current + dir
        if grid.grid[next] == ".":
            graph.add(current, next)
        current = next

    return graph, start


def part1(inp: str) -> int:
    graph, start = parse_input(inp)
    return min_score(map, start)
