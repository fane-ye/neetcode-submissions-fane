class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_s = 0
        for i in range(n):
            count = {}
            maxf = 0
            for j in range(i , n):
                count[s[j]] = count.get(s[j], 0) + 1
                maxf = max(maxf, count[s[j]])
                diff = (j - i + 1) - maxf
                if diff <= k:
                    max_s = max(max_s, j - i + 1)
        return max_s

                




        