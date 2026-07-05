You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

# Solution
# DP 

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        N = len(board)
        MOD = 10 ** 9 + 7
        directions = [
            (-1,0),(0,-1),(-1,-1)
        ]
        grid = [[None] * N for _ in range(N)]
        for i in range(N):
            s = board[i]
            j = 0
            while j < N:
                grid[i][j] = s[j]
                j += 1
        INF = 10 ** 20
        @cache
        def dp(i,j):
            if i == 0 and j == 0:
                return (0,1)
            best = -INF
            count = 0
            for dx,dy in directions:
                nx,ny = i + dx,j + dy
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != "X":
                    score,ways = dp(nx,ny)
                    if score == -INF:
                        continue
                    if ways == 0:
                        return [0,0]
                    score += int(grid[i][j]) if grid[i][j] != "S" else 0
                    if score > best:
                        best = score
                        count = ways
                    elif score == best:
                        count += ways
                        count %= MOD
            return (best,count)
        r = dp(N -  1,N - 1)
        if r[-1] == 0:
            return [0,0]
        return r
        
                
