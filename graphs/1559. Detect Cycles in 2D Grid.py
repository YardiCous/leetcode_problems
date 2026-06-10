# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.
#
# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.
#
# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.
#
# Return true if any cycle of the same value exists in grid, otherwise, return false.


# Solution
# Just a dfs 
# TC: O(M * N) 
# SC: O(M * N) 


from typing import List
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows,cols = len(grid),len(grid[0])
        res = False
        directions = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]
        count = [[-1] * cols for _ in range(rows)]
        def dfs(r,c,depth,char):
            if r < 0 or r == rows or c < 0 or c == cols or char != grid[r][c]:
                return
            if count[r][c] != -1:
                if depth - count[r][c] >= 4:
                    nonlocal res 
                    res = True
                return
            count[r][c] = depth
            for v,u in directions:
                dfs(r + v,c + u,depth + 1,char)
        for r in range(rows):
            for c in range(cols):
                if count[r][c] == -1:
                    dfs(r,c,0,grid[r][c])
                if res == True:
                    break
        return res

    # ["c","a","d"],
    # ["a","a","a"],
    # ["a","a","d"],
    # ["a","c","d"],
    # ["a","b","c"]]
