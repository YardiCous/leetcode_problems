# A subsequence is stable if it does not contain three consecutive elements with the same parity when the subsequence is read in order (i.e., consecutive inside the subsequence).
#
# Return the number of stable subsequences.
#
# Since the answer may be too large, return it modulo 109 + 7.

# Solution
# DP with take and no take, however subsequence is always a problem for me as I cannot visualize how to add from the back so this is a weakness of me
# I also thought it was a math question, and tried to figure out the formula but end up is just DP not happy with myself for this as it was pretty obvious

# Solution
# TC: O(N)
# SC: O(N)


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7
        dp = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]
        for i in range(3):
            for j in range(3):
                dp[N][i][j] = 1
        for i in range(N - 1,-1,-1):
            for j in range(3):
                for k in range(3):
                    res = dp[i + 1][j][k]
                    x = nums[i] % 2
                    if j == 2 and k == 2:
                        res += dp[i + 1][x][2]
                    elif j != 2 and k == 2:
                        res += dp[i + 1][x][j]
                    else:
                        if not(x == j == k):
                            res += dp[i + 1][x][j]
                    dp[i][j][k] = res % MOD
        return (dp[0][2][2] - 1) % MOD
        
        # @lru_cache(None)
        # def dp(i,prev,prevprev):
        #     if i == N:
        #         return 1
        #     res = dp(i + 1,prev,prevprev)
        #     x = nums[i] % 2
        #     if prev == None and prevprev == None:
        #         res += dp(i + 1,x,None)
        #     elif prev is not None and prevprev == None:
        #         res += dp(i + 1,x,prev)
        #     else:
        #         if prev == prevprev == x:
        #             pass
        #         else:
        #             res += dp(i + 1,x,prev)
        #     return res % MOD
        # r = (dp(0,None,None) - 1) % MOD
        # dp.cache_clear()
        # return r
