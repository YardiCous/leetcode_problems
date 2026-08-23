You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

# Solution
# Principle of Inclusion and Exclusion interesting problem and basically for this inclusison exclusion theory
# you want to remove the common numbers that appear and the math is lets say size of N is 3
# it alternates from postive to negative to positive so just create a mask which will go through all of the intercepts 

# TC: O(2 ^ N * N * Log(10 ** 20))

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        N = len(coins)
        def good(x):
            res = 0
            for mask in range(1,1 << N):
                count = 0
                g = 1
                for i in range(N):
                    if mask & (1 << i):
                        count += 1
                        g = lcm(g,coins[i])
                total = x // g
                if count % 2 == 1:
                    res += total
                else:
                    res -= total
            return res >= k
        mn = min(coins)
        left,right = mn,10 ** 20

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid 
            else:
                left = mid + 1
        return left
