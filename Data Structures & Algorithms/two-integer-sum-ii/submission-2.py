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
		
		

		
# def threesum(nums):
# 	res = []
# 	nums.sort()
# 	n = len(nums)
	
# 	for i in range(n):
# 		target = -nums
# 		j, k = i + 1, n - 1
# 		while j < k:
# 			_sum = nums[j] + nums[k]
# 			if _sum > target:
# 				R -=1
# 			elif _sum < target:
# 				L += 1
# 			else:
# 				res.append([nums[i], nums[j], nums[k]])