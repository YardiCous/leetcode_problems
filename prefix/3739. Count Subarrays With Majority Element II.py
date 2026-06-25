# You are given an integer array nums and an integer target.
#
# Return the number of of nums in which target is the majority element.
#
# The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.


# Solution
# Treat target as +1 and all other number as -1
# Use a SortedList or a BIT to keep track of the number of subarrays smaller then the prefix sum of the running current
# Also BIT not so familiar with it but will try learning.

# TC: O(N Log N)
# SC: O(N)


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        sl = SortedList()
        sl.add(0)
        curr = 0
        res = 0
        for x in nums:
            curr += 1 if x == target else -1
            res += sl.bisect_left(curr)
            sl.add(curr)
        return res

class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        offset = N + 1
        curr = 0
        res = 0
        bit = BIT(2 * N + 3)
        bit.add(offset,1)
        for x in nums:
            curr += 1 if x == target else -1

            idx = curr + offset
            res += bit.query(idx - 1)
            bit.add(idx,1)
        return res
