"""
Program: LCS and Edit Distance using Dynamic Programming
Author: Shrey Tiwari

Description:
1. longestCommonSubsequence() finds the length of the
   longest common subsequence between two strings.

2. minDistance() finds the minimum number of insertions,
   deletions, and replacements required to convert one
   string into another.
"""
def longestCommonSubsequence(text1: str, text2: str) -> int:

    m = len(text1)
    n = len(text2)

    # DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


def minDistance(word1: str, word2: str) -> int:

    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1]

            else:

                insert = dp[i][j - 1]
                delete = dp[i - 1][j]
                replace = dp[i - 1][j - 1]

                dp[i][j] = 1 + min(
                    insert,
                    delete,
                    replace
                )

    return dp[m][n]

text1 = input("Enter first string for LCS: ")
text2 = input("Enter second string for LCS: ")

lcs_result = longestCommonSubsequence(text1, text2)

print("Length of Longest Common Subsequence:", lcs_result)


word1 = input("\nEnter first word for Edit Distance: ")
word2 = input("Enter second word for Edit Distance: ")

distance = minDistance(word1, word2)

print("Minimum Edit Distance:", distance)