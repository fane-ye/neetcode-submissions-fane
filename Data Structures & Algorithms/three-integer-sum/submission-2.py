class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[j] + nums[k]
                if _sum > target:
                    k -=1
                elif _sum < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res