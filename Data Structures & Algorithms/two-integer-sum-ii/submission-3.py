class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        L, R = 0, len(nums) - 1
        
        while L < R:
            _sum = nums[L] + nums[R]
            
            if _sum > target:
                R -=1
            
            elif _sum < target:
                L += 1
            
            else:
                return [L + 1, R + 1]
		
		