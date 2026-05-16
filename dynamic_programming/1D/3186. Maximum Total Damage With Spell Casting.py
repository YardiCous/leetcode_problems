# A magician has various spells.
#
# You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
#
# It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
#
# Each spell can be cast only once.
#
# Return the maximum possible total damage that a magician can cast.

# Solution, at first I thought I can solve it greedily but turns out it was dynamic programming

# TC: O(N)
# SC: O(N)


from collections import defaultdict
from functools import lru_cache
from typing import List
class TopDown:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += n
        power = sorted(count.keys())
        N = len(power)
        @lru_cache(None)
        def dfs(i):
            if i == N:
                return 0
            res = dfs(i + 1)
            take = count[power[i]]
            j = i + 1
            while j < N and power[j] - power[i] <= 2:
                j += 1
            take += dfs(j)
            res = max(res,take)
            return res
        r = dfs(0)
        dfs.cache_clear()
        return r
class BottomUp:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += n
        power = sorted(count.keys())
        N = len(power)
        dp = [10 ** 20] * (N + 1)
        dp[-1] = 0
        for i in range(N - 1,-1,-1):
            take = count[power[i]]
            j = i + 1
            while j < N and power[j] - power[i] <= 2:
                j += 1
            take += dp[j]
            dp[i] = max(take,dp[i + 1])
        return dp[0]

