# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #at each level
        #look at nodes
        #get the rightmost node from that level as that is visible
        out = []
        if not root:
            return out
        
        q = deque()
        q.append(root)
        while q:
            line = []
            for i in range(len(q)): #iterate through all nodes in current line
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
                line.append(curr)
            out.append(line[-1].val) #get the rightmost node in line
        return out
