# There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.
#
# Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.
#
# The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.
#
# You are given a 2D integer array queries. For each queries[i] = [ui, vi], determine the number of ways to assign weights to edges in the path such that the cost of the path between ui and vi is odd.
#
# Return an array answer, where answer[i] is the number of valid assignments for queries[i].
#
# Since the answer may be large, apply modulo 109 + 7 to each answer[i].
#
# Note: For each query, disregard all edges not in the path between node ui and vi.

# Solution
# Binary lifting to reduce the N factor to log N Factor, honestly I have no clue how the code works but I get the idea of binary lifing basically, LCA in log N
# Will definitely watch some videos on it 

# TC: O(N log N)
# SC: O(N)


from typing import List
from collections import defaultdict
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        N = len(edges) + 1
        M = N.bit_length()
        MAX = 10 ** 5
        INF = 10 ** 20
        mp = [0] * (MAX + 1)
        mp[0] = 1
        for i in range(1,MAX + 1):
            mp[i] = (mp[i - 1] * 2) % MOD
        adj_list = defaultdict(list)
        for v,u in edges:
            v -= 1
            u -= 1
            adj_list[v].append(u)
            adj_list[u].append(v)
        timer = 0
        timer_in = [None] * N
        timer_out = [None] * N
        dist = [None] * N
        parents = [[None] * N for _ in range(M)]
        def go(node,parent,d):
            nonlocal timer
            timer += 1
            timer_in[node] = timer
            dist[node] = d

            parents[0][node] = parent
            for i in range(1,M):
                parents[i][node] = parents[i - 1][parents[i - 1][node]]
            for nei in adj_list[node]:
                if nei != parent:
                    go(nei,node,d + 1)
            timer += 1
            timer_out[node] = timer
        go(0,0,0)
        def is_anc(node,panc):
            return timer_in[panc] <= timer_in[node] and timer_out[node] <= timer_out[panc]
    
        def distance(node1,node2):
            meet = lca(node1,node2)
            return dist[node1] + dist[node2] - 2 * dist[meet]
        def lca(node1,node2):
            if is_anc(node1,node2):
                return node2
            if is_anc(node2,node1):
                return node1
            for i in range(M - 1,-1,-1):
                if not is_anc(node2,parents[i][node1]):
                    node1 = parents[i][node1]
            return parents[0][node1]
        res = []
        for node1,node2 in queries:
            node1 -= 1
            node2 -= 1
            if node1 == node2:
                res.append(0)
                continue
            direct = distance(node1,node2)
            res.append(mp[direct - 1])
        return res

        


