class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -1 * nums[i]

            # THIS PREVENTS DUPLICATE TRIPLETS
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            while j < k:
                total = nums[j] + nums[k]
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    numj = nums[j]


                    # THIS ALSO PREVENTS DUPLICATE TRIPLETS
                    while j < k and nums[j] == numj:
                        j += 1
                
                    k -= 1

        return res
