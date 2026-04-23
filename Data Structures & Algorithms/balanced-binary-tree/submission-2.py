# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # rooted at the root of a subtree
        # i need to return whether my subtrees are balanced or not
        # i need the height of the left and right subtree
        
        #if height diff > 1, set he

        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0

            lh = dfs(node.left)
            if not balanced:
                return
            rh = dfs(node.right)
            if not balanced:
                return
           
            if abs(lh - rh) > 1:
                balanced = False

            return max(lh, rh) + 1
        dfs(root)
        return balanced
                
        
