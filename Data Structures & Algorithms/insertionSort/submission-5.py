# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # for each position i from 1,n
        # check if that element is smaller than left element
        # if not, keep comparing until it is smaller
        print_list = []
        if pairs: print_list.append(pairs[:]) # initial list
        for i in range(1,len(pairs)):
            j = i - 1
            while j>= 0 and pairs[j + 1].key < pairs[j].key:
                print("j: ",j)
                tmp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = tmp
                j-=1
            print_list.append(pairs[:]) #show list after each insertion 

        return print_list

        