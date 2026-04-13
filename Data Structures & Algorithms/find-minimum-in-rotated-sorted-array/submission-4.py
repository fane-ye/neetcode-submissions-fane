class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        #find sorted half
        while l <= r:
            mid = (l + r) // 2

            #left half is sroted
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1

            #rhs sorted
            else:
                res = min(res, nums[mid + 1])
                r = mid

        return res
                

                

            #right hafl sorted

        #find sorted half, get the smalles element

        #then explore other halfkeep racking of min unil you you explore
        #all sored parts min
        