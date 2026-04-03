# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head
        while curr:
            curr = curr.next
            i += 1
        
        end = i
        print("end", end)
        print("target", end - n)
        curr = head
        prev = None
        for j in range(end - n):
            prev = curr
            curr = curr.next
        
        #at the target node
        #edge case, we remove the head node
        if prev is None and curr.next:
            return curr.next

        elif prev is None:
            return None
        prev.next = curr.next

        return head
            
        