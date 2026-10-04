"""
Program: Huffman Coding
Author: Shrey Tiwari

Description:
Builds a Huffman Tree from character frequencies and
generates binary Huffman codes for each character.
"""

import heapq
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Node:
    char: Optional[str]
    frequency: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class HuffmanCoder:

    def __init__(self):
        self.root = None

    def build_tree(self, frequencies: Dict[str, int]) -> Node:

        heap = []
        counter = 0

        for char, frequency in frequencies.items():
            node = Node(char, frequency)

            heapq.heappush(
                heap,
                (frequency, counter, node)
            )

            counter += 1

        while len(heap) > 1:

            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            new_node = Node(
                None,
                freq1 + freq2,
                left,
                right
            )

            heapq.heappush(
                heap,
                (new_node.frequency, counter, new_node)
            )

            counter += 1

        self.root = heap[0][2]

        return self.root

    def generate_codes(self) -> Dict[str, str]:

        codes = {}

        def generate(node, code):

            if node is None:
                return

            if node.char is not None:
                codes[node.char] = code
                return

            generate(node.left, code + "0")
            generate(node.right, code + "1")

        generate(self.root, "")

        return codes


frequencies = {}

n = int(input("Enter number of characters: "))

print("Enter character and frequency:")

for _ in range(n):

    char, frequency = input().split()

    frequencies[char] = int(frequency)


coder = HuffmanCoder()

coder.build_tree(frequencies)

codes = coder.generate_codes()


print("\nHuffman Codes:")

for char, code in codes.items():
    print(char, ":", code)