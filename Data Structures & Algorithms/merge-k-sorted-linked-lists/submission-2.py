# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current_merged = lists[0] if lists else None
        k = 1
        while k < len(lists): #k times
            list_b = lists[k]
            list_a = current_merged
            current_merged = self.merge_two(current_merged, list_b)
            k+=1

        return current_merged 
    
    def merge_two(self, list_a, list_b):
        dummy_head = ListNode()
        cur = dummy_head        
        temp_sorted = None
        # merge lists
        while list_a and list_b:
            if list_a.val <= list_b.val:
                cur.next = list_a                    
                list_a = list_a.next
            else:
                cur.next = list_b
                list_b = list_b.next
            cur = cur.next

        if list_a is None:
            cur.next = list_b
        else:
            cur.next = list_a

        return dummy_head.next #to get actual head
