# You are given a 0-indexed integer array nums and an integer x.
#
# Find the minimum absolute difference between two elements in the array that are at least x indices apart.
#
# In other words, find two indices i and j such that abs(i - j) >= x and abs(nums[i] - nums[j]) is minimized.
#
# Return an integer denoting the minimum absolute difference between two elements that are at least x indices apart.

# Solution
# Knew how to do it but have to use SortedList which I have not used before
# TC: O(N log N)
# SC: O(N)

from sortedcontainers import SortedList
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        sl = SortedList()
        res = INF
        for i in range(x,N):
            sl.add(nums[i - x])
            idx = sl.bisect_left(nums[i])
            if idx - 1 >= 0:
                res = min(abs(sl[idx - 1] - nums[i]),res)
            if idx < len(sl):
                res = min(abs(sl[idx] - nums[i]), res)
        return res 


        
