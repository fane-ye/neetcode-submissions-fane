class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_s = 0
        i, j = 0, 0
        count = {}
        maxf = 0
        while i < n and j < n:
            count[s[j]] = count.get(s[j], 0) + 1
            maxf = max(maxf, count[s[j]])
            diff = (j - i + 1) - maxf
            if diff <= k:
                max_s = max(max_s, j - i + 1)
                j += 1
            else:
                count[s[j]] -= 1
                count[s[i]] -= 1
                i += 1
        return max_s

                




        