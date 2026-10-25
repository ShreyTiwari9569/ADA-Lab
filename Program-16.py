
"""
Program: KMP String Matching and Reservoir Sampling
Author: Shrey Tiwari

Description:
1. strStr() uses the KMP algorithm to find the first occurrence
   of a pattern in a text.
2. Randomizer.getRandom() uses reservoir sampling to select
   one element uniformly from a stream of integers.
"""

from typing import List
import random

def strStr(haystack: str, needle: str) -> int:

    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    lps = [0] * m
    length = 0
    i = 1

    while i < m:

        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    i = 0
    j = 0

    while i < n:

        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == m:
                return i - j

        elif j != 0:
            j = lps[j - 1]

        else:
            i += 1

    return -1

class Randomizer:

    def __init__(self, stream: List[int]):
        self.stream = stream

    def getRandom(self) -> int:

        selected = None

        for i, value in enumerate(self.stream):
            if random.randrange(i + 1) == 0:
                selected = value

        if selected is None:
            raise ValueError("Stream is empty")

        return selected

haystack = input("Enter text: ")
needle = input("Enter pattern: ")

index = strStr(haystack, needle)

print("\n Pattern found at index:", index)

n = int(input("\n Enter number of stream elements: "))

stream = list(
    map(int, input("Enter stream elements: ").split())
)

if len(stream) != n:
    print("Error: Number of elements does not match.")
else:
    randomizer = Randomizer(stream)
    print("\n Randomly selected element:", randomizer.getRandom())
