from dataclasses import dataclass
from typing import List


@dataclass
class Edge:
    u: int
    v: int
    weight: int


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append(Edge(u, v, weight))

    def kruskal_mst(self) -> List[Edge]:
        parent = list(range(self.vertices + 1))
        rank = [0] * (self.vertices + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        sorted_edges = sorted(self.edges, key=lambda edge: edge.weight)

        mst = []

        for edge in sorted_edges:
            if union(edge.u, edge.v):
                mst.append(edge)

                if len(mst) == self.vertices - 1:
                    break

        return mst

    def prim_mst(self) -> List[Edge]:
        visited = [False] * (self.vertices + 1)
        mst = []

        # Start from vertex 0
        visited[1] = True

        while len(mst) < self.vertices - 1:
            minimum_edge = None

            for edge in self.edges:
                if visited[edge.u] and not visited[edge.v]:
                    if minimum_edge is None or edge.weight < minimum_edge.weight:
                        minimum_edge = edge

                elif visited[edge.v] and not visited[edge.u]:
                    if minimum_edge is None or edge.weight < minimum_edge.weight:
                        minimum_edge = edge

            if minimum_edge is None:
                break

            mst.append(minimum_edge)

            visited[minimum_edge.u] = True
            visited[minimum_edge.v] = True

        return mst


def print_mst(mst: List[Edge]):
    total_weight = 0

    for edge in mst:
        print(f"{edge.u} -- {edge.v} : {edge.weight}")
        total_weight += edge.weight

    print("Total MST weight:", total_weight)


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

g = Graph(n)

print("Enter edges (u v weight):")

for _ in range(m):
    u, v, weight = map(int, input().split())
    g.add_edge(u, v, weight)

print("\nKruskal MST:")
kruskal_result = g.kruskal_mst()
print_mst(kruskal_result)

print("\nPrim MST:")
prim_result = g.prim_mst()
print_mst(prim_result)