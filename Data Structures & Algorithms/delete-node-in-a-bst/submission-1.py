# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: #node not found
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)


        else: #we found the node we want to delete
            #case with 2 children, put smallest if right, biggest if left in place, then delete child
            if root.left and root.right:
                #replace with smallest in right subtree
                minNode = self.getMinNode(root.right)
                root.val = minNode.val

                #delete minNode
                root.right = self.deleteNode(root.right, minNode.val)
                return root

            #case where 0, 1 children, parent node connects to child node/NOne
            else:
                child = root.left if root.right is None else root.right
                root = child

        #return the node of the subtree
        return root

    def getMinNode(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr