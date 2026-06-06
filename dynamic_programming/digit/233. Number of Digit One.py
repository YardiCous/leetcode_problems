# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


# Solution 
# Digit DP

# TC: O(10 * 2 * 2 * 10)
# SC: O(400)

from functools import lru_cache
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        N = len(s)
        @lru_cache(None)
        def dp(index,tight,start,ones):
            if index == N:
                return ones
            limit = int(s[index]) if tight else 9
            res = 0 
            for d in range(limit + 1):
                next_start = start or (d != 0)
                next_tight = tight and (d == limit)
                if not next_start:
                    res += dp(index + 1,next_tight,next_start,ones)
                else:
                    if d == 1:
                        res += dp(index + 1,next_tight,next_start,ones + 1)
                    else:
                        res += dp(index + 1,next_tight,next_start,ones)
            return res
        return dp(0,1,0,0)


