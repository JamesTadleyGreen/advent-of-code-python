from collections import defaultdict


class Graph:
    def __init__(self):
        self._graph = defaultdict(set)

    def add(self, node1, node2=None):
        if node2 is None:
            self._graph[node1] = set()
        else:
            self._graph[node1].add(node2)

    def get_neighbours(self, node):
        return self._graph[node]
