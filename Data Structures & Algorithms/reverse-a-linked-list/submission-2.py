# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case, there is no node or 1 node
        if head is None or head.next is None:
            return head #this is the prev tail, and new head

        # recursive case, first reverse the rest of the list, the pointer swap at this level
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
        


# 0 -> 1 -> 2 -> 3
# head = 0 call: self.reverseList(0) 
# head = 1 call: self.reverseList(1) 
# head - 2: call: self.reverseList(2) 
# head=3: return head(3)