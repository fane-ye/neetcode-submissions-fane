# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # the function will return a sorted list, given a list
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]: 
        n = len(pairs)
        if n <= 1: #base case
            print("basecase: ", [{item.key, item.value} for item in pairs[:]])
            return pairs[:]
        
        # If i have the 2sorted subarrays, I will then run a algorithm to return 
        # the 2 sorted subarrays as one sorted arary
        m = n//2
        
        a = self.mergeSort(pairs[0:m])
        b = self.mergeSort(pairs[m:n])
        ordered = self.order(a, b) 
        print("ordered: ", [{item.key, item.value} for item in ordered])
        return ordered

    def order(self, a: List[Pair], b: List[Pair]):
        print("func order: a, b",[{item.key, item.value} for item in a], [{item.key, item.value} for item in b] )
        sorted_list = []
        i, j = 0, 0
        while i < len(a) and j<len(b):
            if a[i].key>b[j].key:
                sorted_list.append(b[j])
                j += 1 
            else:
                sorted_list.append(a[i])
                i += 1 
        if i == len(a): # if list a exhaused
            sorted_list.extend(b[j:])
            
        elif j == len(b): # if list b exhausted
            sorted_list.extend(a[i:])            
        return sorted_list
