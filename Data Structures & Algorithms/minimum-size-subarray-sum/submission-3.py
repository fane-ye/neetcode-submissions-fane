class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        min_size = len(nums) + 1 #unreachable solutoin
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                min_size = min(min_size, r - l + 1)
                total -= nums[l]
                l += 1

        return min_size if min_size != len(nums) + 1 else 0                    