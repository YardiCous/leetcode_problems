# There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
#
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
#
# Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
#
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.
#
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

# Solution
# BFS/DFS with parity will be enough, I did not know of the parity idea had to ask GPT how to know if two nodes are connected in even length, then it told me about the parity

# TC:O(N)
# SC:O(N)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def solve(edges):
            N = len(edges) + 1
            parity = [-1] * N
            adj_list = defaultdict(list)
            for v,u in edges:
                adj_list[v].append(u)
                adj_list[u].append(v)
            q = collections.deque()
            q.append((0,0))
            visit = set()
            visit.add(0)
            while q:
                depth,node = q.popleft()
                if depth % 2 == 0:
                    parity[node] = 0
                else:
                    parity[node] = 1
                for neiNode in adj_list[node]:
                    if neiNode not in visit:
                        q.append((depth + 1,neiNode))
                        visit.add(neiNode)
            return parity
        p1 = solve(edges1)
        p2 = solve(edges2)
        evens1 = p1.count(0)
        odds1 = p1.count(1)
        evens2 = p2.count(1)
        odds2 = p2.count(0)
        two = max(evens2,odds2)
        res = []
        N = len(edges1) + 1
        for i in range(N):
            if p1[i]:
                res.append(odds1 + two)
            else:
                res.append(evens1 + two)
        return res
