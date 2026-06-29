There is an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node.

You start with a score of 0. In one operation, you can:

    Pick any node i.
    Add values[i] to your score.
    Set values[i] to 0.

A tree is healthy if the sum of values on the path from the root to any leaf node is different than zero.

Return the maximum score you can obtain after performing these operations on the tree any number of times so that it remains healthy.

# Solution
# Tree DP, but I had a hard time thinking of the recursive state had to ask AI for help

# TC: O(N)
# SC: O(N)

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        adj_list = defaultdict(list)
        for v,u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        def dfs(node,par):
            total = values[node]
            mn = 0
            for neiNode in adj_list[node]:
                if neiNode == par:
                    continue
                child_t,child_mn = dfs(neiNode,node)
                total += child_t
                mn += child_mn
            if mn == 0:
                return (total,total)
            mn = min(values[node],mn)
            return (total,mn)
        t,m = dfs(0,-1)
        return t - m

