# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
#
# Each queries[i] represents the following action on nums:
#
#     Decrement the value at each index in the range [li, ri] in nums by at most vali.
#     The amount by which each value is decremented can be chosen independently for each index.
#
# A Zero Array is an array with all its elements equal to 0.
#
# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

# Solution
# Binary search on answer and using a diff array, I thought I had to to use like segment tree, but a diff array is enough

# TC: O(N log M)
# SC: O(N)


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        # total = sum(nums)
        INF = 10 ** 20
        M = len(queries)
        left,right = 0,M + 1

        def good(k):
            diff = [0] * (N + 1)
            for i in range(k):
                left,right,val = queries[i]
                diff[left] += val
                diff[right + 1] -= val
            curr = 0
            for j in range(N):
                curr += diff[j]
                if curr < nums[j]:
                    return False
            return True
        res = -1
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                res = mid
                right = mid
            else:
                left = mid + 1
        return res
