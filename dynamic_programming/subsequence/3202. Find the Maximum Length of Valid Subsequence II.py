# You are given an integer array nums and a positive integer k.
#
# A sub of nums with length x is called valid if it satisfies:
#
#     (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
#
# Return the length of the longest valid subsequence of nums. 

# Solution
# Subsequence DP, I am terrible with it definitely need more work on it.

# TC: O(N * K)
# SC: O(N)
    
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        for i in range(N):
            nums[i] %= k
        # print(nums)
        res = -INF
        for v in range(k):
            dp = [0] * k
            for x in nums:
                prev = v - x
                # print(prev)
                dp[x] = max(dp[x],dp[prev] + 1)
                # print(dp)
            res = max(res,max(dp))
        return res



