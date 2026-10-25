
"""
Program: N-Queens Problem using Backtracking
Author: Shrey Tiwari

Description:
Places N queens on an N x N chessboard so that no two queens
attack each other. Returns all valid board configurations.
"""

from typing import List


def solveNQueens(n: int) -> List[List[str]]:

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    columns = set()
    diagonal1 = set()  # row - column
    diagonal2 = set()  # row + column

    def backtrack(row: int):

        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):

            if (col in columns or
                    row - col in diagonal1 or
                    row + col in diagonal2):
                continue

            board[row][col] = 'Q'
            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            backtrack(row + 1)

            board[row][col] = '.'
            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

    if n > 0:
        backtrack(0)

    return result

n = int(input("Enter board dimension (N): "))

solutions = solveNQueens(n)

print("\nTotal solutions:", len(solutions))

for index, solution in enumerate(solutions, start=1):

    print(f"\nSolution {index}:")

    for row in solution:
        print(row)
