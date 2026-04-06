class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(len(s)):
            maxf = 0
            freq = defaultdict(int)
            for j in range(i, len(s)):
                freq[s[j]] += 1
                maxf = max(maxf, freq[s[j]])

                if j - i + 1 - maxf <= k:
                    max_len = max(max_len, j - i + 1)
        return max_len
                    
                
        