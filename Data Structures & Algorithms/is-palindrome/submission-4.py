class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make lower case and remove non-alphanumeric characters
        l = 0
        r = len(s) - 1

        while l<=r:
            #skip if not alnum
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            #if alnum, compare lower

            else:
                if s[l].lower() != s[r].lower():
                    return False   
                l += 1
                r -= 1
        return True