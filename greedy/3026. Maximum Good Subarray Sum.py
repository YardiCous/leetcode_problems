# You are given an array nums of length n and a positive integer k.
#
# A subarray  of nums is called good if the absolute difference between its first and last element is exactly k, in other words, the subarray nums[i..j] is good if |nums[i] - nums[j]| == k.
#
# Return the maximum sum of a good subarray of nums. If there are no good subarrays, return 0.

# Solution
# The idea for prefix sum is basically finding if n + k and n - k exists in our prefix if it is, take the running total and subtract away the ones we do not want
# the catch is when duplicates, we want to find the minimum suffix sum of the value since the question wants the maximum total subarray

# TC: O(N)
# SC: O(N)

from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10 ** 20
        res = -INF
        total = 0
        prefix = {}
        for n in nums:
            if n in prefix:
                prefix[n] = min(prefix[n],total)
            else:
                prefix[n] = total
            total += n
            for y in [n + k,n - k]:
                if y in prefix:
                    res = max(res,total - prefix[y])
        return res if res != -INF else 0

        
