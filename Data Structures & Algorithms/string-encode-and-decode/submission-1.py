class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for _str in strs:
            res = res + str(len(_str)) + "#" + _str

        return res
    def decode(self, s: str) -> List[str]:
        num = ''
        res = []
        i = 0
        while i < (len(s)):
            num += s[i]
            if s[i] == "#":
                num = num[:-1]
                j = 0
                _str = ''
                i += 1
                while j < int(num):
                    _str += s[i]
                    j += 1
                    i += 1
                i -= 1
                res.append(_str)
                num = ''
            i += 1
        return res
                
            

