# Given two positive integers low and high represented as strings, find the count of stepping numbers in the inclusive range [low, high].
#
# A stepping number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.
#
# Return an integer denoting the count of stepping numbers in the inclusive range [low, high].
#
# Since the answer may be very large, return it modulo 109 + 7.
#
# Note: A stepping number should not have a leading zero.

# Solution
# Digit DP

# TC: O(101 * 4 * 10)
# SC: O(101 * 4 * 10)

from functools import lru_cache
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7
        def solve(num):
            s = str(num)
            N = len(s)
            @lru_cache(None)
            def dp(index,tight,start,prev):
                if index == N:
                    return 1
                limit = int(s[index]) if tight else 9
                res = 0
                for d in range(limit + 1):
                    next_start = start or (d != 0) 
                    next_tight = tight and (d == limit)
                    if not next_start:
                        res += dp(index + 1,next_tight,next_start,-1)
                    elif not start and next_start:
                        res += dp(index + 1,next_tight,next_start,d)
                    else:
                        if prev != -1 and abs(prev - d) == 1:
                            res += dp(index + 1,next_tight,next_start,d)
                return res
            return dp(0,1,0,-1) 
            
        # print(solve(100))
        return (solve(int(high)) - solve(int(low) - 1)) % MOD
