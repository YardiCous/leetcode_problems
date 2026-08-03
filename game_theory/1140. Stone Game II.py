Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        prefix = [0]
        for x in piles:
            prefix.append(prefix[-1] + x)
        @cache
        def dp(index,M):
            if index == N:
                return 0
            # print(M)
            res = 0
            right = index + (2 * M)
            mn = min(N,right)
            # print(index,mn)
            for i in range(index,mn):
                res = max(res,prefix[N] - prefix[index] - dp(i + 1,max(M,i - index + 1)))
            return res
        return dp(0,1)
