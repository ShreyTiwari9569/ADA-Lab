"""
Program: Floyd-Warshall and Optimal BST
Author: Shrey Tiwari

Description:
1. Floyd-Warshall finds shortest paths between all pairs of vertices.
2. Optimal BST finds the minimum search cost of a binary search tree
   based on key frequencies.
"""
from typing import List

def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:

    n = len(graph)

    distance = [row[:] for row in graph]

    for k in range(n):

        for i in range(n):

            for j in range(n):

                if distance[i][k] + distance[k][j] < distance[i][j]:

                    distance[i][j] = (
                        distance[i][k] + distance[k][j]
                    )

    return distance

def optimal_bst(keys: List[int], freq: List[int]) -> int:

    n = len(keys)

    dp = [[0] * n for _ in range(n)]

    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + freq[i]

    for i in range(n):
        dp[i][i] = freq[i]
    for length in range(2, n + 1):

        for i in range(n - length + 1):

            j = i + length - 1

            dp[i][j] = float('inf')

            total_freq = prefix[j + 1] - prefix[i]

            for r in range(i, j + 1):

                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                cost = left + right + total_freq

                dp[i][j] = min(
                    dp[i][j],
                    cost
                )

    return dp[0][n - 1]

n = int(input("Enter number of vertices: "))

print("Enter the distance matrix:")
print("Use 0 for same vertex and INF for no direct edge.")

graph = []

for i in range(n):

    row = input().split()

    converted_row = []

    for value in row:

        if value.upper() == "INF":
            converted_row.append(float('inf'))
        else:
            converted_row.append(int(value))

    graph.append(converted_row)


result = floyd_warshall(graph)


print("\nShortest Path Matrix:")

for row in result:

    print(
        " ".join(
            "INF" if value == float('inf') else str(value)
            for value in row
        )
    )
m = int(input("\nEnter number of keys: "))

keys = list(
    map(int, input("Enter keys: ").split())
)

freq = list(
    map(int, input("Enter frequencies: ").split())
)


cost = optimal_bst(keys, freq)

print("Minimum cost of Optimal BST:", cost)