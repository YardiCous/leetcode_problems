# You are given two positive integers, l and r. A positive integer is called beautiful if the product of its digits is divisible by the sum of its digits.
#
# Return the count of beautiful numbers between l and r, inclusive.

# Solution
# Just digit dp but for some reason 580 is considered special

# TC: O(10 * 2 * 2 * 90 * 90)
# SC: Same as TC

from functools import lru_cache
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def solve(n):
            s = str(n)
            N = len(s)
            @lru_cache(None)
            def dp(index,tight,start,product,total):
                if index == N:
                    if product and total:
                        if product % total == 0:
                            return 1
                    if product == 0:
                        return 1
                    return 0

                limit = int(s[index]) if tight else 9
                res = 0
                for d in range(limit + 1):
                    next_tight = tight and (d == limit)
                    next_start = start or (d != 0)
                    if not next_start:
                        res += dp(index + 1,next_tight,next_start,product,total)
                    else:
                        if d != 0:
                            if product == 0:
                                res += dp(index + 1,next_tight,next_start,0,total)
                            else:
                                res += dp(index + 1,next_tight,next_start,product * d,total + d)
                        else:
                            res += dp(index + 1,next_tight,next_start,0,total)
                return res
            
            return dp(0,1,0,1,0)
        return solve(r) - solve(l - 1)
