class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_s = 0
        for i in range(n):
            for j in range(i , n):
                count = {}
                sub = s[i:j + 1]
                for c in sub:
                    count[c] = count.get(c, 0) + 1

                maxf = max(count.values())
                diff = (j - i + 1) - maxf
                if diff <= k:
                    max_s = max(max_s, j - i + 1)
        return max_s

                




        