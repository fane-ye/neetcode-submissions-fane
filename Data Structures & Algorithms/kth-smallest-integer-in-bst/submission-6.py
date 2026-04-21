# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        res = 0
        def dfs(node):
            nonlocal i
            nonlocal res
            if not node:
                return

            if res != 0:
                return
            dfs(node.left)
            i += 1
            print("i: ", i)
            if i == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
        