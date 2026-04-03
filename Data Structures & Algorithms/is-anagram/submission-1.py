class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for c in s:
            if c not in s_hash:
                s_hash[c] = 1
            else:
                s_hash[c] += 1

        for c in t:
            if c not in t_hash:
                t_hash[c] = 1
            else:
                t_hash[c] += 1

        for key, value in s_hash.items():
            if key not in t_hash:
                return False
            elif value != t_hash[key]:
                return False
        for key, value in t_hash.items():
            if key not in s_hash:
                return False
            elif value != s_hash[key]:
                return False
        return True
        #tip think through all data structures ik and see what suits