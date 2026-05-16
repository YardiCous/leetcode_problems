# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#
#     [4,5,6,7,0,1,4] if it was rotated 4 times.
#     [0,1,4,4,5,6,7] if it was rotated 7 times.
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.

# Solution
# Binary Search and if there is duplicates, decrement right pointer

# TC: Average O(log N) worse case O(N)
# SC: O(1)

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
