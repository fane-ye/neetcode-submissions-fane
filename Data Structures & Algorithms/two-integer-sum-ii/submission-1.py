class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        nums = numbers
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]] = i + 1
            
        for i in range(n):
            rem = target - nums[i]
            if rem in hashmap and hashmap[rem] != i:
                return [i + 1, hashmap[rem]]
		

# def soln2(nums, target):
# 	L = 0
# 	R = len(nums) - 1
	
# 	while L < R:
# 		_sum = nums[L] + nums[R]
		
# 		if _sum > target:
# 			R -=1
		
# 		elif _sum < target:
# 			L += 1
		
# 		else:
# 			return [L, R]
		
		
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