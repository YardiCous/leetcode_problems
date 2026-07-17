You are given three integers m, n, and k.

Construct any m x n grid consisting only of the characters '.' and '#', where:

    '.' represents a free cell.
    '#' represents an obstacle cell.

A valid path is a sequence of free cells that:

    Starts at the top-left cell (0, 0).
    Ends at the bottom-right cell (m - 1, n - 1).
    Moves only:
        Right, from (i, j) to (i, j + 1), or
        Down, from (i, j) to (i + 1, j).

Return any grid such that there are exactly k valid paths from the top-left cell to the bottom-right cell. If no such grid exists, return an empty array.


# Solution
# Retarded Question


class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        rows,cols = m,n
        if (rows == 1 or cols) == 1 and k > 1:
            return []
        if k == 1:
            grid = [["#"] * cols for _ in range(rows)]
            for c in range(cols):
                grid[0][c] = "."
            for r in range(rows):
                grid[r][-1] = "."
            return ["".join(row) for row in grid]
        if k == 2:
            grid = [["#"] * cols for _ in range(rows)]
            for c in range(cols):
                grid[0][c] = "."
            for r in range(rows):
                grid[r][-1] = "."
            grid[1][-2] = "."
            return ["".join(row) for row in grid]
        if k == 3:
            if rows <= 2 and cols <= 2:
                return []
            if rows == 2 and cols == 3:
                grid = [["."] * cols for _ in range(rows)]
                return ["".join(row) for row in grid]
            if cols <= 2:
                grid = [["#"] * cols for _ in range(rows)]
                for r in range(3):
                    for c in range(cols):
                        grid[r][c] = "."
                for r in range(3,rows):
                    grid[r][-1] = "."
                return ["".join(row) for row in grid]
               

            grid = [["#"] * cols for _ in range(rows)]
            for r in range(2):
                for c in range(3):
                    grid[r][c] = "."
            for c in range(3,cols):
                grid[1][c] = "."
            for r in range(2,rows):
                grid[r][-1] = "."
            return ["".join(row) for row in grid]
         
        if k == 4:
            if rows <= 2 and cols <= 3:
                return []
            if rows <= 2:
                grid = [["#"] * cols for _ in range(rows)]
                for c in range(0,4):
                    grid[0][c] = "."
                for c in range(cols):
                    grid[1][c] = "."
                return ["".join(row) for row in grid] 
            if cols <= 2:
                if rows < 4:
                    return []
                grid = [["#"] * cols for _ in range(rows)]
                for r in range(4):
                    for c in range(cols):
                        grid[r][c] = "."
                for r in range(4,rows):
                    grid[r][-1] = "."
                return ["".join(row) for row in grid]
           
            grid = [["#"] * cols for _ in range(rows)]
            grid[0][1] = grid[0][0] = "."
            for c in range(3):
                grid[1][c] = "."
            for c in range(1,cols):
                grid[2][c] = "."
            for r in range(3,rows):
                grid[r][-1] = "."
            return ["".join(row) for row in grid]
          
            "..###"
            "...##"
            "#...."
            "####."
