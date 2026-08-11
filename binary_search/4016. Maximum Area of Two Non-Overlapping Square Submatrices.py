You are given a 2D integer matrix mat of size m × n, where:

    mat[r][c] == 1 means the cell at row r and column c is usable.
    mat[r][c] == 0 means it is not usable.

Your task is to find two that satisfy the following conditions:

    Both submatrices must be squares of the same side length k.
    The two submatrices must not share any cell.
    Each submatrix can only cover cells where mat[r][c] == 1.

Return the maximum possible area of each of the two squares. If it is not possible to choose two such squares, return 0.

# Solution
# Binary search on answer + DP 

# TC: O(N * Log(N))
# SC: O(N)
# N = 500 * 500
class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        rows,cols = len(mat),len(mat[0])
        dp = [[0] * cols for _ in range(rows)]
        for c in range(cols):
            dp[-1][c] = mat[-1][c]
        for r in range(rows):
            dp[r][-1] = mat[r][-1]
        for x in range(rows - 2,-1,-1):
            for y in range(cols - 2,-1,-1):
                if mat[x][y] == 1:
                    dp[x][y] = min(dp[x + 1][y],dp[x][y + 1],dp[x + 1][y + 1]) + 1
        # print(dp)
        def good(k):
            r = SortedList()
            c = SortedList()
            for x in range(rows):
                for y in range(cols):
                    if dp[x][y] == k:
                        r.add(x)
                        c.add(y)
            for index,x in enumerate(r):
                if r[0] <= x - k or r[-1] >= x + k:
                    if index != 0 and r[0] <= x - k:
                        return True
                    if index != len(r) - 1 and r[-1] >= x + k:
                        return True
            for index,y in enumerate(c):
                if c[0] <= x - k or c[-1] >= y + k:
                    if index != 0 and c[0] <= y - k:
                        return True
                    if index != len(c) - 1 and c[-1] >= y + k:
                        return True
            return False
                
        left = 0
        right = (rows * cols) // 2
        res = 0
        while left <= right:
            mid = (left + right + 1) // 2
            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res ** 2

