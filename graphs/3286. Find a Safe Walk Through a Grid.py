You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

# Solution
# 0-1 BFS or Djikstra

# TC: O(N) for BFS O(N Log N) for djikstra
# SC: O(N)

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows,cols = len(grid),len(grid[0])
        directions = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]
        INF = 10 ** 20
        q = deque()
        q.append((0,0))
        dist = [[INF] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        while q:
            r,c = q.popleft()
            for dx,dy in directions:
                nx,ny = dx + r,dy + c
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx][ny] == INF:
                    delta = grid[nx][ny]
                    if delta + dist[r][c] < health:
                        if delta:
                            q.append((nx,ny))
                        else:
                            q.appendleft((nx,ny))
                        dist[nx][ny] = delta + dist[r][c]
        return dist[-1][-1] < health
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows,cols = len(grid),len(grid[0])
        directions = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]
        if grid[0][0] == 1:
            health -= 1
        
        pq = [(-health,0,0)]
        visit = set()
        while pq:
            curr,r,c = heapq.heappop(pq)
            curr *= -1
            if r == rows - 1 and c == cols - 1:
                return True
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dx,dy in directions:
                nx,ny = dx + r, dy + c
                if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in visit:
                    new_curr = curr - grid[nx][ny]
                    if new_curr > 0:
                        heapq.heappush(pq,(-new_curr,nx,ny))
        return False
