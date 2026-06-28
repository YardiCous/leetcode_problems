You are given a 0-indexed array nums consisting of positive integers.

A partition of an array into one or more contiguous subarrays is called good if no two subarrays contain the same number.

Return the total number of good partitions of nums.

Since the answer may be large, return it modulo 109 + 7.

# Solution
# I couldn't think of how track the last number where is it at, didn't think of the end trick, but I identified how to do it
# also the merging part is 2 ^ choices because we can either not merge or merge for any subarray

# TC: O(N)
# SC: O(N)

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7
        end = defaultdict(list)
        for i,x in enumerate(nums):
            end[x] = i
        res = 0
        curr = 0
        for i,x in enumerate(nums):
            curr = max(curr,end[x])
            if curr == i:
                res += 1
        return pow(2,res - 1,MOD)
