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
        curr = slow
        #at the target node
        #edge case, we remove the head node
        if prev is None and curr.next:
            return curr.next

        elif prev is None:
            return None
        prev.next = curr.next

        return head
            
        