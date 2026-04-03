class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        max_s = 0
        count = {}
        maxf = 0
        while r < len(s):
            c = s[r]
            count[c] = count.get(c, 0) + 1
            maxf = max(maxf, count[c])
            #increment l if diff > k
            
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            max_s = max(max_s, r - l + 1)
            r += 1
        return max_s