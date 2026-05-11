# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
#
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
#
# While moving from building i to building i+1 (0-indexed),
#
#     If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#     If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
#
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# Solution
# So the idea is, for every time we are met with a heights[i] > heights[i + 1] we want to ask ourselves, should we use bricks or ladders, well optimally we want to always use the ladders for the biggest
# diff so that we can go as far as possible. With a heap data structure, we can keep track of the length of the heap, when it exceeds the ladders, we can pop the smallest diff and use the bricks
# Had to ask LLM to walk me through, basically I ask it questions, and also check the hint sections


# TC: O(N log N)
# SC: O(N)


from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        minHeap = []
        # print(maxHeap)
        for i in range(N - 1):
            if heights[i] < heights[i + 1]:
                diff = heights[i + 1] - heights[i]
                heapq.heappush(minHeap,diff)
                # print(minHeap)
                if len(minHeap) > ladders:
                    diff = heapq.heappop(minHeap)
                    bricks -= diff
                    if bricks < 0:
                        return i
                # print(bricks)
        return N - 1
