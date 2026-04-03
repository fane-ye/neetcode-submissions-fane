class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_s = 0
        i, j = 0, 0
        count = {}
        maxf = 0
        for j in range(n):
            count[s[j]] = count.get(s[j], 0) + 1
            maxf = max(maxf, count[s[j]])
            
            while (j - i + 1) - maxf > k:
                count[s[i]] -= 1
                i += 1
                maxf = max(count.values()) if count else 0

            max_s = max(max_s, j - i + 1)
                
        return max_s

                




        