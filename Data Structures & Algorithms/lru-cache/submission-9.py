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
            prev_node = accessed_node.prev
            next_node = accessed_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            #remove node then insert at end
            last_node = self.tail.prev
            last_node.next = accessed_node
            accessed_node.next = self.tail
            accessed_node.prev = last_node
            self.tail.prev = accessed_node
            # print("getting key: ", key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.get(key) # Move to MRU position
            return
    
        #if no capacity
        if len(self.cache) == self.capacity:
            #evict LRU
            #remove at ll start
            lru_node = self.head.next
            self.head.next = lru_node.next
            lru_node.next.prev = self.head
            del self.cache[lru_node.key]
            del self.address_map[lru_node.key]

        #when there is capacity
        self.cache[key] = value
        #insert at ll end
        new_node = Node(key, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.address_map[key] = new_node