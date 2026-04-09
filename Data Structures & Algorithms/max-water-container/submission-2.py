class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                h = min(height[i], height[j])
                max_area = max(max_area, (j - i) * h)
        return max_area