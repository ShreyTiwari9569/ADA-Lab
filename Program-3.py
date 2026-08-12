def findKthLargest(nums: list[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


def findMinMax(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)


# Example
nums = [7, 2, 9, 4, 1, 6]

k = 3

print("Kth Largest:", findKthLargest(nums, k))
print("Min-Max:", findMinMax(nums))