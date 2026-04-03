class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #construct hash map O(n)
        hashmap = {}
        for i in range(len(nums)):
            # if nums[i] not in hashmap:
            hashmap[nums[i]] = i 
        #iterate through nums, target-num, search in O(1) time for required num, n times
        for i in range(len(nums)):
            res = []
            res.append(i)
            req = target - nums[i]
            if req in hashmap:
                print(hashmap[req])
                if hashmap[req] == i:
                    continue
                res.append(hashmap[req])
                return res