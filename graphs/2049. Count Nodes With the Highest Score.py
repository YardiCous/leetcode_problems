There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.


# Solution
# DFS 

# TC: O(N)
# SC: O(N)

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        res = [0] * N
        adj_list = defaultdict(list)
        for i in range(N):
            if i == 0:
                continue
            adj_list[parents[i]].append(i)
        def dfs(node,par):
            nonlocal res
            score = 1
            subtree = 1
            for neiNode in adj_list[node]:
                if node != par:
                    size = dfs(neiNode,node)
                    score *= size
                    subtree += size
            if score == 1 and subtree == 1:
                res[node] = N - 1
                return 1
            remain = N - subtree
            if remain:
                score *= remain
            res[node] = score
            return subtree
        dfs(0,-1)
        mx = max(res)
        return res.count(mx)

