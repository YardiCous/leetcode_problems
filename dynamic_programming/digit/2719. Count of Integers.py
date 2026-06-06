# You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:
#
#     num1 <= x <= num2
#     min_sum <= digit_sum(x) <= max_sum.
#
# Return the number of good integers. Since the answer may be large, return it modulo 109 + 7.
#
# Note that digit_sum(x) denotes the sum of the digits of x.


# Solution
# Digit DP

# TC: O(23 * 2 * 2 *23 * 9)
# SC: O(23 * 2 * 2 * 23 * 9)

from functools import lru_cache
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        def solve(num):
            s = str(num)
            N = len(s)
            @lru_cache(None)
            def dp(index,tight,start,total):
                if index == N:
                    if min_sum <= total <= max_sum:
                        return 1
                    return 0
                limit = int(s[index]) if tight else 9
                res = 0
                for d in range(limit + 1):
                    next_start = start or (d != 0)
                    next_tight = tight and (d == limit)
                    if not next_start:
                        res = res + dp(index + 1,next_tight,next_start,total)
                    else:
                        res = res + dp(index + 1,next_tight,next_start,total + d)
                return res
            return dp(0,1,0,0)
    


        return (solve(int(num2)) - solve(int(num1) - 1)) % MOD
