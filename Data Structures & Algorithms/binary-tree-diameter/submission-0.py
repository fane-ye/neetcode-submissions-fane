# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diam = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_max_path = dfs(node.left)
            right_max_path = dfs(node.right)
            print("L: ", left_max_path)
            print("R: ", right_max_path)
            self.max_diam = max(self.max_diam,left_max_path + right_max_path)

            return max(left_max_path, right_max_path) + 1

        dfs(root)
        return self.max_diam
        