# There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.
#
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.
#
# Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.
#
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.
#
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

# Solution
# BFS from every node then the max dist from second tree, pretty simple the only difficult part of this problem is the description

# TC: O(N ^ 2 + M ^ 2)
# SC: O(N + M)


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        N = len(edges1) + 1
        M = len(edges2) + 1

        dist_N = [0] * N
        dist_M = [0] * M
        adjN_list = defaultdict(list)
        adjM_list = defaultdict(list)
        for v,u in edges1:
            adjN_list[v].append(u)
            adjN_list[u].append(v)
        for v,u in edges2:
            adjM_list[v].append(u)
            adjM_list[u].append(v)
        def bfs(start,j,adj_list):
            q = deque()
            q.append((0,start))
            count = 0
            visit = set()
            visit.add(start)
            while q:
                # print(q)
                dist,node = q.popleft()
                count += 1
                for neiNode in adj_list[node]:
                    if neiNode not in visit and dist + 1 <= j:
                        q.append((dist + 1,neiNode))
                        visit.add(neiNode)
            return count
        for i in range(N):
            dist_N[i] = bfs(i,k,adjN_list)
        for i in range(M):
            dist_M[i] = bfs(i,k - 1,adjM_list)
        # print(dist_N)
        # print(dist_M)
        res = []
        mx = max(dist_M)
        for i in range(N):
            if k == 0:
                res.append(dist_N[i])
            elif k == 1:
                res.append(dist_N[i] + 1)
            else:
                res.append(mx + dist_N[i])
        return res
