# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        current_merged = lists[0]
        for k in range(1, len(lists)):
            current_merged = self._merge_two(current_merged, lists[k])
        return current_merged

    def _merge_two(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()          # new list head
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next        # advance tail!

        tail.next = a if a else b   # append remainder
        return dummy.next
