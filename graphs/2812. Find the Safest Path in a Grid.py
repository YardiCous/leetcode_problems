You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

    A cell containing a thief if grid[r][c] = 1
    An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.


# Solution
# Multi source BFS and Djikstra or Binary search on target

# TC: O(M * N Log (M + N))
# SC: O(M * N)


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        directions = [
            (1,0),(0,1),(-1,0),(0,-1)
        ]
        INF = 10 ** 20
        new_grid = [[INF] * cols for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
                    new_grid[i][j] = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dx,dy in directions:
                    dr,dc = dx + r,dy + c
                    if 0 <= dr < rows and 0 <= dc < cols:
                        if new_grid[dr][dc] == INF:
                            new_grid[dr][dc] = new_grid[r][c] + 1
                            q.append((dr,dc))
        pq = [(-new_grid[0][0],0,0)]
        dist = [[INF] * cols for _ in range(rows)]
        dist[0][0] = new_grid[0][0]
        while pq:
            cost,r,c = heapq.heappop(pq)
            cost *= -1
            if cost < dist[r][c]:
                continue
            for dx,dy in directions:
                dr,dc = dx + r,dy + c
                if 0 <= dr < rows and 0 <= dc < cols:
                    if new_grid[dr][dc] < dist[dr][dc]:
                        new_cost = min(cost,new_grid[dr][dc])
                        heapq.heappush(pq,(-new_cost,dr,dc))
                        dist[dr][dc] = new_cost
        return dist[-1][-1]

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        directions = [
            (1,0),(0,1),(-1,0),(0,-1)
        ]
        mx = 0
        INF = 10 ** 20
        new_grid = [[INF] * cols for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
                    new_grid[i][j] = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dx,dy in directions:
                    dr,dc = dx + r,dy + c
                    if 0 <= dr < rows and 0 <= dc < cols:
                        if new_grid[dr][dc] == INF:
                            new_grid[dr][dc] = new_grid[r][c] + 1
                            mx = max(mx,new_grid[r][c] + 1)
                            q.append((dr,dc))
        def good(target):
            q = deque()
            seen = [[False] * cols for _ in range(rows)]
            if new_grid[0][0] >= target:
                q.append((0,0))
                seen[0][0] = True
            while q:
                r,c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dx,dy in directions:
                    dr,dc = dx + r,dy + c
                    if 0 <= dr < rows and 0 <= dc < cols:
                        if new_grid[dr][dc] >= target and seen[dr][dc] == False:
                            q.append((dr,dc))
                            seen[dr][dc] = True
            return False
        left,right = 0, cols + 1
        while left < right:
            mid = (left + right + 1) // 2
            if good(mid):
                left = mid
            else:
                right = mid - 1
        return left
