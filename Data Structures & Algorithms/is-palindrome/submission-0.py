class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make lower case and remove non-alphanumeric characters
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())

        n = len(s)

        for i in range(n//2):
            if s[i] != s[n-1-i]:
                print("wrong char", s[i], s[n-1-i])
                return False

        return True