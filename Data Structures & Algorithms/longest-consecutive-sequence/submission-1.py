class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        prev_num = [num - 1 for num in nums]


        seq_start = []
        for n in prev_num: #O(n)
            if n not in hashset: #O(1)
                seq_start.append(n+1)

        max_seq = 0
        for num in seq_start:
            n = 0
            while num in hashset: #O(1)
                num += 1
                n += 1
            max_seq = max(n, max_seq)
        return max_seq