# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if root is None:
            return out

        #do first level
        q = deque()
        q.append(root)
        level = 1

        #process the queue, invariant, if the queue is not empty, print the queue
        while q:
            #pop queue until empty
            level_out = []
            for i in range(len(q)):
                curr_node = q.popleft()
                #at each level keep adding left and right if exists 
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                    
                level_out.append(curr_node)

            out.append([node.val for node in level_out])
        return out
        