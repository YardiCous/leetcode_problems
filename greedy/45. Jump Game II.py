# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
#
#     0 <= j <= nums[i] and
#     i + j < n
#
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

# Solution
# First thought was DP but I know there is a greedy way
# TC for DP
# TC: O(N * M) where N = length of nums and M is max of nums
# SC: O(N)

# TC for greedy
# TC: O(N) 
# SC: O(1)

from typing import List
class IterativeDP:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [10 ** 20] * N
        dp[0] = 0

        for i in range(N):
            for j in range(i + 1,min(N,i + nums[i] + 1)):
                dp[j] = min(dp[j],dp[i] + 1)
        return dp[N - 1] 

class Solution1:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        left,right = 0,0
        res = 0
        goal = 0
        # for i in range()
        while right < N - 1:
            for i in range(left,right + 1):
                goal = max(nums[i] + i,goal)
            left = right + 1
            right = goal
            res += 1
        return res

from functools import lru_cache
# Top Down DP
class TopDown:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        @lru_cache(None)
        def dfs(i):
            if i >= N - 1:
                return 0
            res = 10 ** 20
            for j in range(i + 1,min(N,i + nums[i] + 1)):
                res = min(res,dfs(j) + 1)
            return res
        return dfs(0)
# BFS solution
from collections import deque
class BFS:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        q = deque()
        q.append((0,0))
        visit = set()   
        while q:
            node,cost = q.popleft()
            if node == N - 1:
                return cost
            if node in visit:
                continue
            visit.add(node)
            for i in range(node + 1,min(N,node + nums[node] + 1)):
                if i not in visit:
                    q.append((i,cost + 1))
        
        return 0
