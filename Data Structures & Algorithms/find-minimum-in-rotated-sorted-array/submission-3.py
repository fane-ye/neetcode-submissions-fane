class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            # If the current window is already sorted, nums[l] is the min
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2

            # Decide which half contains the pivot (and thus the minimum)
            if nums[mid] > nums[r]:
                # mid is in the left (higher) sorted block; min is to the right
                l = mid + 1
            else:
                # mid is in the right (lower) block; min is at mid or to the left
                r = mid

        return nums[l]