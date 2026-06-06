# You are given an m x n integer matrix grid.
#
# Two players move across the grid:
#
#     Player 1 starts at the top-left cell (0, 0) and can move only right or down. Their destination is the bottom-right cell (m - 1, n - 1).
#     Player 2 starts at the bottom-left cell (m - 1, 0) and can move only right or up. Their destination is the top-right cell (0, n - 1).
#
# Each player must choose a valid path from their respective starting cell to their destination.
#
# A cell is called shared if it belongs to both chosen paths.
#
# Return an integer denoting the maximum possible sum of values of all shared cells.

# Solution
# The idea is kadane, but with a twist, if the intersection is around the borders, minimumlly two cells are inserted, but if intersection occurs
# inside the border, only 1 cell can be intersected, so just use kadane for that, most difficult part is the proof of the borders and realizing that the question
# requires kadane rather than dp,dfs,bfs

# TC:O(M * N)
# SC:O(1)

from typing import List
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = -(10 ** 20)
        for r in range(rows):
            curr = grid[r][0]
            for c in range(1,cols):
                total = curr + grid[r][c]
                res = max(res,total)
                if r > 0 and r < rows - 1 and c > 0 and c < cols - 1:
                    res = max(res,grid[r][c])
                curr = max(grid[r][c],total)
        for c in range(cols):
            curr = grid[0][c]
            for r in range(1,rows):
                total = curr + grid[r][c]
                res = max(res,total)
                if r > 0 and r < rows - 1 and c > 0 and c < cols - 1:
                    res = max(res,grid[r][c])
                curr = max(grid[r][c],total)
        return res
