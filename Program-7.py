"""
Program: Shortest Path Algorithms
Author: Shrey Tiwari

Description:
Implements:
1. Dijkstra's Algorithm
2. Bellman-Ford Algorithm

Both methods take a source vertex and return the
shortest distance from the source to every vertex.

Bellman-Ford also detects negative weight cycles.
"""

from typing import List


class ShortestPath:

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    # Add directed edge
    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))

    def dijkstra(self, src: int) -> List[int]:

        INF = float('inf')

        distance = [INF] * (self.vertices + 1)
        visited = [False] * (self.vertices + 1)

        distance[src] = 0

        for _ in range(self.vertices):

            u = -1
            minimum = INF

            for i in range(1, self.vertices + 1):
                if not visited[i] and distance[i] < minimum:
                    minimum = distance[i]
                    u = i

            if u == -1:
                break

            visited[u] = True

            for edge_u, edge_v, weight in self.edges:

                if edge_u == u and not visited[edge_v]:

                    if distance[u] + weight < distance[edge_v]:
                        distance[edge_v] = distance[u] + weight

        return distance[1:]

    def bellman_ford(self, src: int) -> List[int]:

        INF = float('inf')

        distance = [INF] * (self.vertices + 1)

        distance[src] = 0

        for _ in range(self.vertices - 1):

            updated = False

            for u, v, weight in self.edges:

                if distance[u] != INF:

                    if distance[u] + weight < distance[v]:

                        distance[v] = distance[u] + weight
                        updated = True

            if not updated:
                break

        for u, v, weight in self.edges:

            if distance[u] != INF and distance[u] + weight < distance[v]:
                return ["Negative cycle detected"]

        return distance[1:]


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

graph = ShortestPath(n)

print("Enter edges (u v weight):")

for _ in range(m):

    u, v, weight = map(int, input().split())

    graph.add_edge(u, v, weight)

src = int(input("Enter source vertex: "))

print("\nDijkstra's Algorithm:")
dijkstra_result = graph.dijkstra(src)

for i in range(n):
    if dijkstra_result[i] == float('inf'):
        print(f"Vertex {i + 1}: INF")
    else:
        print(f"Vertex {i + 1}: {dijkstra_result[i]}")

print("\nBellman-Ford Algorithm:")
bellman_result = graph.bellman_ford(src)

if bellman_result and bellman_result[0] == "Negative cycle detected":

    print("Error: Negative weight cycle detected.")

else:

    for i in range(n):
        if bellman_result[i] == float('inf'):
            print(f"Vertex {i + 1}: INF")
        else:
            print(f"Vertex {i + 1}: {bellman_result[i]}")