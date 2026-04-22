# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #rooted at the root of a subtree
        #save temp, node.left=node.right, node.right = node.left
        #recurse down 
        #return

        def dfs(node):
            if not node:
                return
            

            tmp = node.left
            node.left = node.right
            node.right = tmp
            dfs(node.left)
            dfs(node.right)

            return 
        dfs(root)
        return root


        