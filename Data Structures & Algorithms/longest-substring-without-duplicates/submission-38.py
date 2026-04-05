class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        #extend window
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in window:
                print("adding: ", s[r])
                window.add(s[r])
                max_len = max(max_len, r - l + 1)
                

            else:
                # max_len = max(max_len, r - l)
                print("left: ", s[l])
                print("right ", s[r])
                while s[l] != s[r]:
                    print("removing: ", s[l])
                    
                    window.remove(s[l])
                    l += 1
                if s[l] == s[r]:
                    l += 1
        return max_len

        #add each char to a hash set as window is extended

        # if the new char is in hashet, record current size

        # move pointer until we find occurence of current new char
        # drop letters from hashset as we pass them
        