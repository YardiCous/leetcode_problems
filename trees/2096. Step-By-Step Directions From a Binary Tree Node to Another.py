# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
#     'L' means to go from a node to its left child node.
#     'R' means to go from a node to its right child node.
#     'U' means to go from a node to its parent node.
#
# Return the step-by-step directions of the shortest path from node s to node t.

# Solution
# First I did a BFS where I converted the tree to graph, but it is not efficient surprisngly, it passed the testcases but it is O(N ^ 2) TC wise so not efficient, the other way to do
# it is by using LCA, well today I learned the purpose of LCA, LCA can be used if you want to find the shortest path between two nodes, since the LCA will be always be found  between these two nodes
# TC:O(N)
# SC:O(N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def dfs(node,val,path):
            if not node:
                return False
            
            if val == node.val:
                return True
            
            path.append("L")
            if dfs(node.left,val,path):
                return True
            path.pop()
            path.append("R")
            if dfs(node.right,val,path):
                return True
            path.pop()
            return False
        start,dest = [],[]
        dfs(root,startValue,start)
        dfs(root,destValue,dest)

        i = 0
        while i < min(len(start),len(dest)) and start[i] == dest[i]:
            i += 1
        return "U" * (len(start) - i) + "".join(dest[i:])
