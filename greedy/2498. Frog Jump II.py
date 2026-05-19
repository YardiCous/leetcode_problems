# You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.
#
# A frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.
#
# The length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.
#
#     More formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.
#
# The cost of a path is the maximum length of a jump among all jumps in the path.
#
# Return the minimum cost of a path for the frog.

# Solution
# The idea that the first frog jumps every even index and second frog jumps odd index, that is the greedy proof need a nudge from LLM though.
# TC: O(N)
# SC: O(1)

from typing import List
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N = len(stones)
        if N == 2:
            return stones[-1]
        res = -(10 ** 20)
        i = 2
        while i < N:
            diff = abs(stones[i] - stones[i - 2])
            res = max(diff,res)
            i += 2
        i = 3
        while i < N:
            diff = abs(stones[i] - stones[i - 2])
            res = max(diff,res)
            i += 2
        return res 

