class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        tmp = None
        for i in range(n // 2):
            j = n - i - 1
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
        

