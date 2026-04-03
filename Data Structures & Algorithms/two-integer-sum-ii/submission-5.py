class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}

        for i in range(len(numbers)):
            nums[numbers[i]] = i
        
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in nums:
                return [i + 1, nums[diff] + 1]
        