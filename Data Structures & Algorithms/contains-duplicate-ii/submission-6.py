class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        [1,2,3,0,2]
        [1,2,3,1]
        # iterate through mantaining a window of size k
        # if number added is in window, return true

        i = 0
        seen = set()
        for j in range(len(nums)):
            if nums[j] in seen:
                return True
            
            seen.add(nums[j])

            if abs(i - j) == k:
                seen.remove(nums[i])
                i += 1

        return False


        