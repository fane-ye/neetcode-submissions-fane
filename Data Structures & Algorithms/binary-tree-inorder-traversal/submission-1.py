# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ordered = []
        self.traverse(root, ordered)
        return ordered
        
        
    def traverse(self, root, ordered):
        if root is None:
            return
        
        self.traverse(root.left, ordered)
        ordered.append(root.val)
        self.traverse(root.right, ordered)

                