You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.


# Solution
# Interval DP


# TC: O(N ^ 3)
# SC: O(N ^ 3)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # N = len(nums)
        nums = [1] + nums + [1]
        N = len(nums)
        @cache
        def dp(i,j):
            if j == i + 1:
                return 0
            res = 0
            for k in range(i + 1,j):
                res = max(res,dp(i,k) + dp(k,j) + nums[i] * nums[k] * nums[j])
            return res
        return dp(0,N - 1)
