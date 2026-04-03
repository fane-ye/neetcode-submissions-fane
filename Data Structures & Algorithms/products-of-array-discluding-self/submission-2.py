class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create prefix array
        prefix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                continue
            prod = prefix[i-1] * nums[i-1]
            prefix.append(prod)

        suffix = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums)-1:
                suffix.append(1)
                continue
            prod = suffix[-1] * nums[i+1]
            suffix.append(prod)
        
        suffix.reverse()
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res