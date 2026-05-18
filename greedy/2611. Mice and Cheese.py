# There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.
#
# A point of the cheese with index i (0-indexed) is:
#
#     reward1[i] if the first mouse eats it.
#     reward2[i] if the second mouse eats it.
#
# You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.
#
# Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.

# Solution 
# The idea is a heap basically find the difference between each reward1[i] - reward2[i] then let first mice run k times then second mice for the rest

# TC: O(N log N)
# SC: O(N)

from typing import List
import heapq
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        N = len(reward1)
        maxH = []
        res = 0
        for i in range(N):
            heapq.heappush(maxH,(-(reward1[i] - reward2[i]),i))
        # print(maxH)
        while k > 0:
            _,index = heapq.heappop(maxH)
            res += reward1[index]
            k -= 1
        while maxH:
            _,index = heapq.heappop(maxH)
            res += reward2[index]
        return res
