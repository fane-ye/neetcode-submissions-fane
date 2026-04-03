# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        for _ in range(n):
            fast = fast.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            
        #edge case, we remove the head node
        if prev is None and slow.next:
            return slow.next
        elif prev is None:
            return None
        prev.next = slow.next

        return head
            
        