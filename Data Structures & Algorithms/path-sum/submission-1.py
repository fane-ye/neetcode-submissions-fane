# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #backtracking
        
        #base case: 
        if root is None:
            return False

        # subtract current node value 
        targetSum -= root.val 

        # Check if current node is a leaf
        if root.left is None and root.right is None and targetSum==0:
            return True

        #otherwise keep going left and right 
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        


        return False
        #returning boolean 