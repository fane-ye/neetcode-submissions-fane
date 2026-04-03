class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1 #O(n)

        freq_occur= [None] * (1 + len(nums))
        for key, value in num_freq.items():
            if freq_occur[value] is None:
                freq_occur[value] = []
            freq_occur[value].append(key)
        res = []
        for j in range(len(nums), 0, -1):
            nums = freq_occur[j]
            if nums:
                for num in nums:
                    res.append(num)
                    k -= 1
                    if k == 0:
                        return res