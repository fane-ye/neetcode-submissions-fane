class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        pos = {}
        #extend window
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in pos and pos[s[r]] >= l:
                l = pos[s[r]] + 1
            
            pos[s[r]] = r
            max_len = max(max_len, r - l + 1)

            
     
        return max_len