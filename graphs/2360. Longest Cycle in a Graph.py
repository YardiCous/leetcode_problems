# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
#
# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.
#
# Return the length of the longest cycle in the graph. If no cycle exists, return -1.
#
# A cycle is a path that starts and ends at the same node.

# Solution
# I have to keep track of local map, previously I did not do that and TLE because of that

# TC: O(N)
# SC: O(N)

from typing import List
from collections import deque
class BFS:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        res = -1
        visit = [False] * N
        
        def bfs(node):
            q = deque()
            q.append((0,node))
            local_visit = {}
            while q:
                depth,index = q.popleft()
                if index in local_visit != -1:
                    nonlocal res
                    res = max(res,depth - local_visit[index])
                if visit[index]:
                    continue
                visit[index] = True
                local_visit[index] = depth
                if edges[index] != -1:
                    q.append((depth + 1,edges[index]))

        for i in range(N):
            if not visit[i] and edges[i] != -1:
                bfs(i)
        return res
class DFS:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        res = -1
        visit = [False] * N
        
        def dfs(node,m,depth):
            if node == -1:
                return
            if node in m:
                nonlocal res
                res = max(res,depth - m[node])
                return
            if visit[node]:
                return
            visit[node] = True
            m[node] = depth
            dfs(edges[node],m,depth + 1)

        for i in range(N):
            if not visit[i]:
                dfs(i,{},0)
        return res
