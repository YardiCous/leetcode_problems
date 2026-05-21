# You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.
#
#     For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
#
# Return the minimum number of operations to make an array that is sorted in non-decreasing order.

# Solution
# The idea is start from the back right since it wants the array to be in ascending order
# and basically if nums[i] can be modded by the smallest we have seen we gucci right just mod it by the smallest
# but if it isnt, we have to split it and greedily choose the highest possible number to split for example
# [9,28,3] since 28 cannot be split into 3s right
# split 28 to 3,3,3,3,3,3,3,3,2,2
# this is 28 // 3 + 1 and to find the smallest now it would be 28 // 10 which is 2

# TC: O(N)
# SC: O(1)

from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        smallest = nums[-1]
        for i in range(N - 2,-1,-1):
            if nums[i] <= smallest:
                smallest = nums[i]
                continue
            if nums[i] % smallest == 0:
                res += (nums[i] // smallest) - 1
            else:
                val = nums[i] // smallest
                res += val
                if nums[i] > 9:
                    smallest = nums[i] // (val + 1)
                else:
                    smallest = nums[i] // (val + 1)
                    # print(smallest)
        return res
