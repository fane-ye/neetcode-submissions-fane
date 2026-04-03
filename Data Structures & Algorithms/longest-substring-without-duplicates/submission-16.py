class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        if n == 0:
            return 0
        j = 1

        max_len = 1
        while j < n:
            if s[j] in s[i:j]: #if char existings in precedeing substr
                max_len = max(max_len, j - i)
                while s[i] != s[j]:
                    i += 1
                i += 1
                
            j += 1
        
        
        return max(max_len, j - i)