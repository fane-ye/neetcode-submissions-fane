class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1

        target_map = [0] * 26
        for c in s1:
            pos = ord(c) - ord('a')
            target_map[pos] += 1
        
        
        while r < len(s2):
            cand_map = [0] * 26
            substr = s2[l:r+1] #slice to r

            for c in substr:
                pos = ord(c) - ord('a')
                cand_map[pos] += 1
            
            if target_map == cand_map:
                return True

            l += 1
            r += 1

        return False