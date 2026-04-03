class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create map
        s1chars = {}
        for c in s1:
            s1chars[c] = s1chars.get(c, 0) + 1
        
        l = r = 0

        matchd = 0
        need = len(s1chars)
        s2chars = {}
        for r in range(len(s2)):

            # add r char
            c = s2[r]
            if c in s1chars and s2chars.get(c, 0) + 1 == s1chars[c]:
                matchd += 1
            s2chars[c] = s2chars.get(c, 0) + 1  #O(1)

            if matchd == need:
                    return True
            
            if r - l + 1 == len(s1):
                #remove l char
                c = s2[l]
                if c in s1chars and s2chars.get(s2[l], 0) == s1chars[c]:
                    matchd -= 1
                s2chars[s2[l]] -= 1
                l += 1

            

            r += 1
        return False


        