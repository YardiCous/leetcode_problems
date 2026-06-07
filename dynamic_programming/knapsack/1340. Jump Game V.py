# Given an array of integers arr and an integer d. In one step you can jump from index i to index:
#
#     i + x where: i + x < arr.length and  0 < x <= d.
#     i - x where: i - x >= 0 and  0 < x <= d.
#
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).
#
# You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.
#
# Notice that you can not jump outside of the array at any time.

# Solution 
# Initially thought of BFS, but DP is the correct answer, I had some issue with my code, particularly the res = 1 and breaking off when nums[i] <= nums[j] and had to look at hints,
# because I did not think of DP

# TC: O(N ^ 2)
# SC: O(N)

from typing import List
from functools import lru_cache
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        INF = 10 ** 20
        @lru_cache(None)
        def dfs(index):
            if index == N or index < 0:
                return 0
            res = 1
            for dx in range(index + 1,index + d + 1):
                if dx < N:
                    if arr[dx] < arr[index]:
                        res = max(res,dfs(dx) + 1)
                    else:
                        break
            for dx in range(index - 1, index - d - 1 ,-1):
                if dx >= 0:
                    if arr[dx] < arr[index]:
                        res = max(res,dfs(dx) + 1)
                    else:
                        break
            return res
        res = -INF
        for i in range(N):
            res = max(res,dfs(i))
        return res
