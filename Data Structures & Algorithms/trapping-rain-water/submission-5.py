class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = []
        n = len(height)
        
        prefix_max.append(0)
        for i in range(1, n):
            prefix_max.append(max(prefix_max[i-1], height[i - 1]))

        suffix_max = [0] * n
        for i in range(n - 1 - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i + 1])
        
        print("prefixs", prefix_max)
        print("suffixes", suffix_max)
        area = 0
        for i in range(n):
            vol = max(0, min(prefix_max[i], suffix_max[i]) - height[i])
            area += vol
        
        return area


        