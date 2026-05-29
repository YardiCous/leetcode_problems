# You are given a 0-indexed integer array nums.
#
# Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:
#
#     Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
#
# Return the maximum possible number of marked indices in nums using the above operation any number of times.

# Solution
# Well the greedy idea is to sort and split the array into two halfs, I actuaLly had this idea, but I couldn't write a proof on this
# only after I watched larry then I realize that I was right.

# TC: O(N log N)
# SC: O(N)
from typing import List
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        N = len(nums)
        left,right = nums[N// 2:], nums[:N//2]
        i,j = 0,0
        res = 0
        while i < len(left) and j < len(right):
            if right[j] >= left[i] * 2:
                i += 1
                j += 1
                res += 2
            else:
                i += 1
        return res
