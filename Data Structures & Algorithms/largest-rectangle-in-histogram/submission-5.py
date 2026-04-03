class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        right_bounds = [n] * n

        for i in range(n - 1, - 1, -1):
            #calculate right bounds

            #pop stack until we get to element that is smaller
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            #once popped calculate
            if stack:
                right_bounds[i] = stack[-1]

            stack.append(i)
        print(right_bounds)

        stack = []
        left_bounds = [-1] * n
        for i in range(0, n):

            #pop stack until we reach element with height smaller
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            #calculate leftmost index
            if stack:
                left_bounds[i] = stack[-1]

            #add to stack
            stack.append(i)
        print(left_bounds)

        area = 0
        for i in range(n):
            l = left_bounds[i]
            r = right_bounds[i]

            area = max(area, (r - l - 1) * heights[i])
            
        return area


        
        