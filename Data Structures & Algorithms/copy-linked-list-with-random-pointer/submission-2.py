"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next22
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through original linked list
        # add to a hashmap
        curr = head
        nodes = {None: None}
        
        if not head:
            return None

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next


        # iterate through old linked list, getting next and random 
        # values from map and getting new nodes and connecting
        curr = head
        while curr:
            #get next value
            new_nxt = nodes[curr.next] 
            #get random value
            new_rand = nodes[curr.random]

            new_node = nodes[curr]
            new_node.next = new_nxt
            new_node.random = new_rand
            curr = curr.next
        return nodes[head]