"""
Program: Longest Increasing Subsequence
Author: Shrey Tiwari

Description:
Finds the length of the longest strictly increasing
subsequence in an integer array.
"""
from typing import List

def lengthOfLIS(nums: List[int]) -> int:

    n = len(nums)

    if n == 0:
        return 0

    dp = [1] * n

    for i in range(n):

        for j in range(i):

            if nums[j] < nums[i]:

                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )

    return max(dp)

n = int(input("Enter number of elements: "))

nums = list(
    map(int, input("Enter elements: ").split())
)

result = lengthOfLIS(nums)

print("Length of Longest Increasing Subsequence:", result)