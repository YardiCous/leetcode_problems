You are given a positive integer k. You are also given:

    a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
    a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].

The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

    The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
    The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.

Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.



# Solution
# TOPO SORT

# TC:O(N * M)
# SC:O(N * M)


class Solution:
    def buildMatrix(self, N: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        grid = [[0] * N for _ in range(N)]
        indexes = defaultdict(list)
        def f(g):
            adj_list = defaultdict(list)
            degree = [0] * (N + 1)
            for v,u in g:
                adj_list[v].append(u)
                # adj_list[u].append(v)
                degree[u] += 1
            q = deque()
            for i in range(1,N + 1):
                if degree[i] == 0:
                    q.append(i)
            i = 0
            if len(q) == 0:
                return
            while q:
                node = q.popleft()
                indexes[node].append(i)
                i += 1
                for neiNode in adj_list[node]:
                    degree[neiNode] -= 1
                    if degree[neiNode] == 0:
                        q.append(neiNode)
        f(rowConditions)
        f(colConditions)
        if len(indexes) == 0:
            return []
        for j in indexes.keys():
            if len(indexes[j]) != 2:
                return []
            x,y = indexes[j]
            grid[x][y] = j
        return grid
