# You are given an undirected graph with n nodes labeled from 0 to n - 1. Node i has a value of nums[i], which is either 0 or 1. The edges of the graph are given by a 2D array edges where edges[i] = [ui, vi] represents an edge between node ui and node vi.
#
# For a non-empty subset s of nodes in the graph, we consider the induced subgraph of s generated as follows:
#
#     We keep only the nodes in s.
#     We keep only the edges whose two endpoints are both in s.
#
# Return an integer representing the number of non-empty subsets s of nodes in the graph such that:
#
#     The induced subgraph of s is connected.
#     The sum of node values in s is even.

# Solution
# Was surprisingly quite easy, but was unable to solve it during the contest
# The idea is generate all subsets and just do a dfs for each subset as the constraints are really small
# Basically combing DFS + Subset backtracking

# TC: O((V + E) * 2 ^ N) 
# SC: O(2 ^ N + E)

from collections import defaultdict
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        N = len(nums)
        s = []
        res = 0
        adj_list = defaultdict(list)
        for v,u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        def good(arr):
            if len(arr) == 0:
                return False
            arr_set = set(arr)
            total = 0
            for n in arr:
                total += nums[n]
            if total % 2:
                return False
            visit = set()
            def dfs(node):
                visit.add(node)
                for neiNode in adj_list[node]:
                    if neiNode in arr_set and neiNode not in visit:
                        dfs(neiNode)
            dfs(arr[0])
            for index in arr:
                if index not in visit:
                    return False
            # print("HERE")
            return True
        def subset(index):
            if index == N:
                if good(s):
                    nonlocal res
                    res += 1
                return
            s.append(index)
            subset(index + 1)
            s.pop()
            subset(index + 1)
        subset(0)
        return res
