class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        l = 0
        window = {}
        have = 0 
        need = len(tCount)
        min_int = [-1, len(s)]
        for r in range(len(s)):

            # add character and check if need to update have
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tCount and tCount[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_int[-1] - min_int[0] + 1:
                    min_int = [l, r]

                # move l up, while have == need
                if s[l] in tCount and window[s[l]] == tCount[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1   

            


        return "" if min_int[0] == -1 else s[min_int[0]: min_int[-1] + 1]





