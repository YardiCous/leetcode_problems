# There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.
#
# Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.
#
# The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.
#
# Select any one node x at the maximum depth. Return the number of ways to assign edge weights in the path from node 1 to x such that its total cost is odd.
#
# Since the answer may be large, return it modulo 109 + 7.
#
# Note: Ignore all edges not in the path from node 1 to x.


# Solution
# bfs from node 1 and get the different combinations, I learned today if 1s and 2s, you can just do 2^edges // 2 because 1 half sums up to even, the other odd

# TC:O(N)
# SC: O(N)

from collections import defaultdict
from typing import List
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        adj_list = defaultdict(list)
        for v,u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        def dfs(node,prev):
            res = 0
            for j in adj_list[node]:
                if j == prev:
                    continue
                res = max(res,dfs(j,node) + 1)
            return res
        d = dfs(1,-1)
        return (2 ** (d - 1)) % (10 ** 9 + 7)

