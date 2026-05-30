# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Solution
# Similarly to diameter tree question, just find the maximum sum of any path by doing a postorder, I had some trouble and also had to realize if there are negatives, can just set
# it to be 0 since we do not want to consider it in a greedy way.

# TC: O(N)
# SC: O(N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        INF = 10 ** 20
        res = -INF
        def dfs(node):
            nonlocal res 
            if not node:
                return 0
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            nonlocal res 
            total = node.val + left + right
            res = max(res,total)
            return node.val + max(left,right)
        dfs(root)
        return res
