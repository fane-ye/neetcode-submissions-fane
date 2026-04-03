class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        last_unique_num = nums[k]
        
        for i in range(len(nums)):
            if last_unique_num != nums[i]:
                last_unique_num = nums[i]
                k+=1
                nums[k] = last_unique_num

        return k + 1

        