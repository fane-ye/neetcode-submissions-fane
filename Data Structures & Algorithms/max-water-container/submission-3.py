class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #start l and r pointer on ends

        #calculate the area at the given l, r
        #update the state of maxA
        #move the index inwards (of whichever has the smaller height)
        

        l = 0
        r = len(heights) - 1
        maxA = 0
        while l <= r:
            height = min(heights[l], heights[r])
            maxA = max(maxA, height * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA

        