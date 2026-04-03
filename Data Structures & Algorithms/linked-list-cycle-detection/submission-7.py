# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp = head
        fp = head
        if fp is None:
            return False
        fp = head.next
        while fp is not None:
            if fp.val == sp.val:
                return True
            
            if fp.next is None:
                return False
            fp = fp.next.next
            sp = sp.next


        return False #fp reached tail
        