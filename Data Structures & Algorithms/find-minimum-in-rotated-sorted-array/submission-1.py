class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(start, end):
            if nums[start] <= nums[end]: #equals accounts for when len==1 as no numbers should be repeated
                return nums[start]
            
            mid = (start + end) // 2
            l_min = find_min(start, mid)
            r_min = find_min(mid + 1, end)
            return min(l_min, r_min)
        return find_min(0, len(nums) - 1)