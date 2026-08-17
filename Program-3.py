def findKthLargest(nums: list[int], k: int) -> int:
    # Sort the list in descending order
    nums.sort(reverse=True)
    
    # Return the element at index k-1
    return nums[k - 1]


# Function to find the minimum and maximum elements
def findMinMax(nums: list[int]) -> tuple[int, int]:
    # Use min() to find the smallest element
    # Use max() to find the largest element
    return min(nums), max(nums)


# Example list
nums = [7, 2, 9, 4, 1, 6]
k = 3

# Display the kth largest element
print("Kth Largest:", findKthLargest(nums, k))

# Display the minimum and maximum elements
print("Min-Max:", findMinMax(nums))
