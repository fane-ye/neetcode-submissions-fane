class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        prev = None

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both pointers
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # delete node
        if prev is None:
            return slow.next  # removing head

        prev.next = slow.next
        return head