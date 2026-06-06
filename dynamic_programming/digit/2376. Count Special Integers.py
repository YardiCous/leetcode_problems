# We call a positive integer special if all of its digits are distinct.
#
# Given a positive integer n, return the number of special integers that belong to the interval [1, n].

# Solution
# Digit DP

# TC(10 * 10 * 2 * 2)
# SC(400)


from functools import lru_cache
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        N = len(s)
        @lru_cache(None)
        def dp(index,tight,mask,start):
            if index == N:
                return 1
            limit = int(s[index]) if tight else 9
            res = 0
            for d in range(limit + 1):
                next_start = start or (d != 0)
                next_tight = tight and (d == limit)

                if not next_start:
                    res += dp(index + 1,next_tight,mask,0)
                else:
                    if mask & (1 << d):
                        continue
                    res += dp(index + 1,next_tight,mask | (1 << d),next_start)
            return res
        return dp(0,1,0,0) - 1
