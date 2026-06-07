# You are given an integer array nums of length n and a binary string s of length n, where s[i] == '1' means index i initially contains a token and s[i] == '0' means it does not.
#
# You may perform the following operation any number of times:
#
#     Choose a token currently located at index i, where i > 0, such that this token has not been moved before.
#     Move this token from index i to index i - 1.
#
# An index is considered covered if it contains a token after all moves.
#
# Return an integer denoting the maximum total value of nums at the covered indices after optimally performing the operations.

# Solution
# Just DP, i was trying to come up with the greedy solution but I couldn't think of it.

# TC: O(N)
# SC: O(N)


from typing import List
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        N = len(nums)
        
        dp = [[0] * 2 for _ in range(N + 1)]
        for i in range(N - 1,-1,-1):
            for p in range(2):
                if s[i] == "1":
                    dp[i][p] = max(dp[i][p],dp[i + 1][0] + nums[i])
                    if p:
                        dp[i][p] = max(dp[i][p],dp[i + 1][p] + nums[i - 1])
                else:
                    dp[i][p] = max(dp[i][p],dp[i + 1][1])
        return dp[0][0]
        # def dp(index,prev):
        #     if index == N:
        #         return 0
        #     res = 0
        #     if s[index] == "1":
        #         res = max(res,dp(index + 1,False) + nums[index])
        #         if prev:
        #             res = max(res,dp(index + 1,True) + nums[index - 1])
        #     else:
        #         res = max(res,dp(index + 1,True))
        #     return res
        # return dp(0,0)
