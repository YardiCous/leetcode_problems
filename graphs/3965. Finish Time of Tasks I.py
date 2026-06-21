# You are given an integer n representing the number of tasks in a project, numbered from 0 to n - 1. These tasks are connected as a tree rooted at task 0. This is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that task ui is the parent of task vi.
#
# You are also given an array baseTime of length n, where baseTime[i] represents the time to complete task i.
#
# The finish time of each task is calculated as follows:
#
#     Leaf task: The finish time is baseTime[i].
#     Non-leaf task:
#         Let earliest be the minimum finish time among its children, and latest be the maximum finish time among its children.
#         Let ownDuration be (latest - earliest) + baseTime[i].
#         The finish time of task i is latest + ownDuration.
#
# Return the finish time of the root task 0.

# Solution
# Just DFS or Topo Sort

# TC: O(N)
# SC: O(N)

class Solution:
    def finishTime(self, N: int, edges: List[List[int]], baseTime: List[int]) -> int:
        INF = 10 ** 20
        adj_list = defaultdict(list)
        for v,u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        def dfs(node,par):
            mx,mn = -INF,INF
            for neiNode in adj_list[node]:
                if neiNode != par:
                    t = dfs(neiNode,node)
                    mx = max(mx,t)
                    mn = min(mn,t)
            if mx == -INF and mn == INF:
                return baseTime[node]
            own_duration = mx - mn + baseTime[node]
            return own_duration + mx
        return dfs(0,-1)

class Solution:
    def finishTime(self, N: int, edges: List[List[int]], baseTime: List[int]) -> int:
        adj_list = defaultdict(list)
        degree = [0] * N
        for v,u in edges:
            adj_list[u].append(v)
            degree[v] += 1
        q = deque()
        dist = [0] * N
        for i in range(N):
            if degree[i] == 0:
                q.append(i)
                dist[i] = baseTime[i]
        visit = defaultdict(list)
        mx = [-inf] * N
        mn = [inf] * N
        while q:
            node = q.popleft()
            for neiNode in adj_list[node]:
                
                mx[neiNode] = max(mx[neiNode],dist[node])
                mn[neiNode] = min(mn[neiNode],dist[node])
                l,e = mx[neiNode],mn[neiNode]
                dist[neiNode] = l - e + baseTime[neiNode] + l
                degree[neiNode] -= 1
                if degree[neiNode] == 0:
                    q.append(neiNode)
        return dist[0]
            
