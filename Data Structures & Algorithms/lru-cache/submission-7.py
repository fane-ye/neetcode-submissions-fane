from collections import deque

class Node:
    def __init__(self, key = None, prev = None, next = None):
        self.key = key
        self.prev = prev
        self.next = next
    
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = {} #key, value
        self.capacity = capacity
        self.address_map = {} #key, Node

        self.head = Node() #LRU
        self.tail = Node() #MRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            #update in ll to be most recently used
            accessed_node = self.address_map[key]
            prev = accessed_node.prev
            next = accessed_node.next
            prev.next = next
            next.prev = prev
            #remove node then insert at end
            tail = self.tail.prev
            tail.next = accessed_node
            accessed_node.next = self.tail
            accessed_node.prev = tail
            self.tail.prev = accessed_node
            # print("getting key: ", key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        
        #if no capacity
        elif len(self.cache) == self.capacity:
            #evict LRU
            #remove at ll start
            head = self.head.next
            self.head.next = head.next
            head.next.prev = self.head
            print("evicting key: ",head.key)
            del self.cache[head.key]
            del self.address_map[head.key]

        print("putting key: ",key)
        #when there is capacity
        self.cache[key] = value
        #insert at ll end
        new_tail = Node(key, self.tail.prev, self.tail)
        self.tail.prev.next = new_tail
        self.tail.prev = new_tail
        self.address_map[key] = new_tail
         