class Solution:
    def validPalindrome(self, s: str) -> bool:
        #iterate with 2 pointers in s, e
        #move pointers in if equal
        #if not equal, 
            # if flag deletion done
                #return false
            #check if l can be incr to bring eql
            #check if r can be decr to bring equal, flag deletion
            
        #return true

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Check if deleting either the left char or the right char works
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
        return True