# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #new_head = min(of heads) 
        #curr_l1 compare with curr_l2
        # new_head.next = min of curr ptrs
        #update curr pointer of min
        # keep going until both curr pointers are None
    
        cur_l1, cur_l2 = list1, list2
        if not cur_l1: return cur_l2
        if not cur_l2: return cur_l1
        if list1.val < list2.val:
            new_head=list1
            cur_l1=list1.next
        else:
            new_head=list2
            cur_l2=list2.next
        new_list_cursor = new_head
        while cur_l1 and cur_l2:
            if cur_l1.val < cur_l2.val:
                new_list_cursor.next = cur_l1
                cur_l1 = cur_l1.next
            else:
                new_list_cursor.next = cur_l2
                cur_l2 = cur_l2.next
            new_list_cursor = new_list_cursor.next
        new_list_cursor.next = cur_l1 if cur_l1 else cur_l2
        return new_head
