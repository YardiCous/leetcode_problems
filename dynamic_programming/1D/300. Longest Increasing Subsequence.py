# Longest Increasing Subsequence
# Medium Topics Company Tags
# Hints
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.
#
#     For example, "cat" is a subsequence of "crabt".

# Solution
# Nested loops and dp search, tried to do it with pruning but didnt work out
# Also through this problem learn to set dp values based on the question requirement at first put as float but had to put as 1 as all positions is a subarray of 1 initially

# TC: O(N ^ 2)
# SC: O(N)

from typing import List
class BottomUp:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        dp[-1] = 1
        for i in range(N - 1,-1,-1):
            for j in range(i + 1,N):    
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)


from functools import lru_cache
class TopDown:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        @lru_cache(None)
        def dfs(i):
            res = 1
            for j in range(i + 1,N):
                if nums[j] > nums[i]:
                    res = max(res,dfs(j) + 1)
            return res
        return max(dfs(i) for i in range(N))
