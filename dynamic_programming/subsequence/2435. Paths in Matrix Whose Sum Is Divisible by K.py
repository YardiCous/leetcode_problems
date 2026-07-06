You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

# Solution
# DP with trick of using % 

# TC: O(N * M * k)
# SC: O(N * M * k)


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows,cols = len(grid),len(grid[0])
        directions = [
            (1,0),(0,1)
        ]
        MOD = 10 ** 9 + 7
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        dp[rows - 1][cols - 1][0] = 1
        for r in range(rows - 1,-1,-1):
            for c in range(cols - 1,-1,-1):
                if r == rows - 1 and c == cols - 1:
                    continue
                for j in range(k):
                    res = 0
                    for dx,dy in directions:
                        nx,ny = dx + r,c + dy
                        if 0 <= nx < rows and 0 <= ny < cols:
                            t = j + grid[nx][ny]
                            t %= k
                            res += dp[nx][ny][t]
                    dp[r][c][j] = res % MOD
        return dp[0][0][grid[0][0] % k]
        # @cache
        # def dp(r,c,total):
        #     if r == rows - 1 and c == cols - 1:
        #         if total == 0:
        #             return 1
        #         return 0
        #     res = 0
        #     for dx,dy in directions:
        #         nx,ny = dx + r,c + dy
        #         if 0 <= nx < rows and 0 <= ny < cols:
        #             t = total + grid[nx][ny]
        #             t %= k
        #             res += dp(nx,ny,t)
        #     return res % MOD
        # return dp(0,0,grid[0][0] % k)
