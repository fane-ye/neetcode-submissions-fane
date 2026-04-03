class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums[0]
        end = nums[-1]
        if start < end or n==1: #asc
            return start

        else: #desc
            left_min = self.findMin(nums[0:n//2])
            right_min = self.findMin(nums[n//2:n])
            return min(left_min, right_min)