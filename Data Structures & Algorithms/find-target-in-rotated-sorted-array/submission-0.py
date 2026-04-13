class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        #half the array, check which side of the array is sorted
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #if left side sored
            if nums[l] <= nums[mid]:
                #check if in left side
                if nums[l] <= target and target <= nums[mid]:
                    #in left side
                    r = mid
                else:
                    #in r side
                    l = mid + 1
            #right side sorted
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
        return -1



            #if right side sored
            
        