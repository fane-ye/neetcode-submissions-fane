from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = []
        #iterate over all elements
        l = r = 0
        while r < len(nums):
            # if num being added is greater than elements in front in deque
            while deq and nums[r] > nums[deq[-1]]:
                deq.pop()
            deq.append(r)

            # if window is size k, append to res
            if r - l + 1 == k:
                # if front of deque elmeents index is out of window
                if deq[0] < l:
                    deq.popleft()
                res.append(nums[deq[0]])
                l += 1
            r += 1
        return res

        