# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

# Solution - Backtracking

# By using a set for res, avoid duplication then, theres two decison for each node, append or skip based on if it is in increasing order

# TC: 2^N
# SC: 2^N

from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(i,temp):
            if i == len(nums):
                if len(temp) >= 2:
                    res.add(tuple(temp))
                return
            if not temp or nums[i] >= temp[-1]:
                temp.append(nums[i])
                backtrack(i + 1,temp)
                temp.pop()
            backtrack(i + 1,temp)
        backtrack(0,[])
        return list(res)


