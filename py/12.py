from collections import defaultdict
from pprint import pprint
from typing import Dict, List, Set


class Graph:
    vertices: Dict[int, str] = {}
    edges: Dict[int, Set[int]] = defaultdict(set)

    def __str__(self) -> str:
        return f"""Graph:
        Vertices: {self.vertices}
        Edges: {self.edges}
        """

    def add_vertex(self, idx: int, data: str):
        self.vertices[idx] = data

    def add_edge(self, idx_from: int, idx_to: int):
        self.edges[idx_from] |= {idx_to}
        self.edges[idx_to] |= {idx_from}


def G():
    g = Graph()
    g.add_vertex(0, "Frankfurt")
    g.add_vertex(1, "Mannheim")
    g.add_vertex(2, "Karlsruhe")
    g.add_vertex(3, "Augsburg")
    g.add_vertex(4, "München")
    g.add_vertex(5, "Nürnberg")
    g.add_vertex(6, "Kassel")
    g.add_vertex(7, "Stuttgart")
    g.add_vertex(8, "Würzburg")
    g.add_vertex(9, "Erfurt")

    g.add_edge(0, 1)
    g.add_edge(0, 8)
    g.add_edge(0, 6)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 6)
    g.add_edge(8, 9)
    g.add_edge(8, 5)
    g.add_edge(5, 7)
    g.add_edge(5, 4)

    return g


def dfs(graph: Graph, v, visited: List, stop):
    visited.append(v)

    print(v, graph.vertices[v])

    for w in graph.edges[v]:
        if w == stop:
            print("found", stop)
        if w not in visited:
            dfs(graph, w, visited, stop)


dfs(G(), 0, [], 3)
