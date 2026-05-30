# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.

# Solution
# Basically get the left sub tree longest path and right subtree longest path and a post order travesal.
# TC: O(N)
# SC: O(N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res
            res = max(res,left + right)
            return 1 + max(left,right)
        dfs(root)
        return res
