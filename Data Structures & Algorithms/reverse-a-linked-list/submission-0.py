# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse through linked list
        # first element, next = None
        # next elements, next is previous elements
        # last element is the new head
        cur = head
        prev = head
        if cur:
            cur = cur.next
        else:
            return head
        while cur:   
            nxt = cur.next         
            cur.next = prev
            prev = cur
            cur = nxt
            
        head.next = None
        return prev

