
"""
Program: Travelling Salesman Problem (TSP)
Author: Shrey Tiwari

Description:
Finds the minimum cost tour that visits every city exactly once
and returns to the starting city using Dynamic Programming.
"""

from typing import List

class TSPSolver:

    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:

        n = len(dist_matrix)

        if n == 0:
            return 0

        if any(len(row) != n for row in dist_matrix):
            raise ValueError("Distance matrix must be square")

        INF = float('inf')
        dp = [[INF] * n for _ in range(1 << n)]

        dp[1][0] = 0

        for mask in range(1 << n):

            for u in range(n):

                if dp[mask][u] == INF:
                    continue

                if not (mask & (1 << u)):
                    continue

                for v in range(n):

                    if not (mask & (1 << v)):

                        new_mask = mask | (1 << v)

                        new_cost = (
                            dp[mask][u] + dist_matrix[u][v]
                        )

                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            new_cost
                        )

        full_mask = (1 << n) - 1

        answer = INF

        for city in range(n):

            if dp[full_mask][city] != INF:
                answer = min(
                    answer,
                    dp[full_mask][city] + dist_matrix[city][0]
                )

        if answer == INF:
            raise ValueError("No complete tour exists")

        return int(answer)

n = int(input("Enter number of cities: "))

print("Enter the distance matrix:")

dist_matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    dist_matrix.append(row)

solver = TSPSolver()

result = solver.solve_tsp(dist_matrix)

print("Minimum tour cost:", result)
