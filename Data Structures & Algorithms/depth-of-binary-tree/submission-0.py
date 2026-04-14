# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        #at node(1) the max depth of its left and right subtree
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        #base case, no node

        return max(left, right) + 1

        

        #if either left or right subtree is not none, return 1
        