class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        def b_search(l, r, target):
            if l > r:
                return -1 #base case/invariant
            
            mid = (l + r) // 2
            if nums[mid] == target: #base case
                return mid 
            elif nums[mid] < target:
                i = b_search(mid+1, r, target)
            elif nums[mid] > target:
                i = b_search(l, mid-1, target)
            return i
            #return index of target or fail -1


        l = 0
        r = len(nums) - 1
        return b_search(l, r, target)
        