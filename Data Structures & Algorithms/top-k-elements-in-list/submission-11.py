class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count freq of numbers in nums
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        #sort freqs
        #make array of size n, where indexes represent freqs
        #put in numbers in each index that have that freq
        n = len(nums)
        array = [[] for i in range(n+1)]
        for num, freq in count.items():
            array[freq].append(num)

        res = []
        #count array backwards until k==0
        for nums in reversed(array):
            for num in nums:
                res.append(num)
                k -= 1
                if k == 0:
                    return res