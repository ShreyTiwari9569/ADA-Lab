
"""
Program: Graph Coloring and Hamiltonian Cycle
Author: Shrey Tiwari

Description:
1. graph_coloring(m) assigns colors to vertices so that
   adjacent vertices have different colors.
2. hamiltonian_cycle() finds a cycle that visits every
   vertex exactly once and returns to the starting vertex.
"""

from typing import List

class GraphBacktracker:

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u: int, v: int):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def graph_coloring(self, m: int) -> List[int]:

        colors = [0] * self.vertices

        def is_safe(vertex, color):

            for neighbor in range(self.vertices):
                if (self.graph[vertex][neighbor] == 1 and
                        colors[neighbor] == color):
                    return False

            return True

        def backtrack(vertex):

            if vertex == self.vertices:
                return True

            for color in range(1, m + 1):

                if is_safe(vertex, color):
                    colors[vertex] = color

                    if backtrack(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        if backtrack(0):
            return colors

        return []

    def hamiltonian_cycle(self) -> List[int]:

        if self.vertices == 0:
            return []

        path = [0] * self.vertices
        path[0] = 0

        def is_safe(vertex, position):

            if self.graph[path[position - 1]][vertex] == 0:
                return False

            if vertex in path[:position]:
                return False

            return True

        def backtrack(position):

            if position == self.vertices:

                return self.graph[path[position - 1]][path[0]] == 1

            for vertex in range(1, self.vertices):

                if is_safe(vertex, position):
                    path[position] = vertex

                    if backtrack(position + 1):
                        return True

                    path[position] = 0

            return False

        if backtrack(1):
            return path + [path[0]]

        return []

n = int(input("Enter number of vertices: "))

g = GraphBacktracker(n)

e = int(input("Enter number of edges: "))

print("Enter edges (u v), using vertices 0 to", n - 1)

for _ in range(e):
    u, v = map(int, input().split())
    g.add_edge(u, v)

# Graph Coloring
m = int(input("Enter number of colors: "))

coloring = g.graph_coloring(m)

if coloring:
    print("\nVertex color mapping:")
    for vertex, color in enumerate(coloring):
        print(f"Vertex {vertex}: Color {color}")
else:
    print("\nNo valid coloring exists.")

cycle = g.hamiltonian_cycle()

if cycle:
    print("\nHamiltonian cycle:", " -> ".join(map(str, cycle)))
else:
    print("\nNo Hamiltonian cycle exists.")
