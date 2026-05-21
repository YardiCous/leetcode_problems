# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.
#
# For chosen indices i0, i1, ..., ik - 1, your score is defined as:
#
#     The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
#     It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
#
# Return the maximum possible score.
#
# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

# Solution
# The idea is that since each subsequence will have to * by the minimum of that subsequence, we can sort by nums2 and use a minHeap to keep track of 
# The biggest numbers we have seen so far and whenever the length of the heap is bigger than k pop the smallest element.

# TC: O(N Log N)
# SC: O(N)

from typing import List
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = list(zip(nums1,nums2))
        nums.sort(key=lambda x:x[1])
        N = len(nums1)
        res,total = 0,0
        minH = []
        for i in range(N - 1,-1,-1):
            heapq.heappush(minH,nums[i][0])
            total += nums[i][0]
            if len(minH) > k:
                total -= heapq.heappop(minH)
            if len(minH) == k:
                res = max(res,total * nums[i][1])
        return res
