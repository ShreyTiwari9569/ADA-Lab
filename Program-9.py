"""
Program: 0/1 Knapsack using Dynamic Programming
Author: Shrey Tiwari

Description:
Finds the maximum value that can be obtained from items
using 0/1 Knapsack.

Each item can either be selected completely or not selected.

Both 2D DP and 1D DP methods are implemented.
"""

from typing import List


def knapsack_01_2d(weights: List[int], values: List[int], capacity: int) -> int:

    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_01_1d(weights: List[int], values: List[int], capacity: int) -> int:

    n = len(weights)

    # 1D DP array
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):

            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )

    return dp[capacity]

n = int(input("Enter number of items: "))

weights = list(
    map(int, input("Enter weights: ").split())
)

values = list(
    map(int, input("Enter values: ").split())
)

capacity = int(
    input("Enter capacity: ")
)


# 2D DP
result_2d = knapsack_01_2d(
    weights,
    values,
    capacity
)

print("\nMaximum value using 2D DP:", result_2d)


# 1D DP
result_1d = knapsack_01_1d(
    weights,
    values,
    capacity
)

print("Maximum value using 1D DP:", result_1d)