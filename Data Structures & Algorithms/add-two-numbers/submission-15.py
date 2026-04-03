# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #find longest list 
        tmp1 = l1
        tmp2 = l2
        while tmp1 and tmp2:
            tmp1, tmp2 = tmp1.next, tmp2.next
    
        long_list = l2 if not tmp1 else l1
        shorter_list = l1 if not tmp1 else l2
        carry = 0

        head = long_list
        while long_list:
            shorter_list_val =  0 if not shorter_list else shorter_list.val 
            _sum = long_list.val + shorter_list_val + carry
            carry = _sum // 10
            long_list.val = _sum % 10
            
            if not long_list.next and carry > 0:
                long_list.next = ListNode(carry)
                break
                
            long_list = long_list.next
            if shorter_list:
                shorter_list = shorter_list.next


        return head