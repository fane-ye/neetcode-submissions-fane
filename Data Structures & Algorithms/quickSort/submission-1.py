# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        #base case, size 1, 0 split
        if len(pairs) <= 1:
            return pairs
        
        
        
        #get pivot
        print([(pair.key, pair.value) for pair in pairs])
        pivot = pairs[-1]

        i = 0 
        j = 0 #insertion pointer
        while i < len(pairs) - 1:
            if pairs[i].key < pivot.key:
                #swap
                tmp = pairs[j]
                pairs[j] = pairs[i]
                pairs[i] = tmp
                j += 1
            i += 1
             

        #locate smaller to left, bigger to right, pivot becomes "centered"
        tmp = pairs[j]
        pairs[j] = pivot
        pairs[-1] = tmp

        print("post_sort", [(item.key, item.value) for item in pairs])

        # split again at pivot value, call quicksort again
        mid = len(pairs)//2
        l = self.quickSort(pairs[:j])
        r = self.quickSort(pairs[j+1:])
        
        # function needs to return sorted array
        return l + [pairs[j]] + r
        