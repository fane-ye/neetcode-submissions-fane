# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            #here is where we get the i'th value
            if i[0] == k:
                val.append(root.val)
                return
            i[0] += 1
            traverse(root.right)

        i = [1]
        val = []
        traverse(root)
        return val[0]

        