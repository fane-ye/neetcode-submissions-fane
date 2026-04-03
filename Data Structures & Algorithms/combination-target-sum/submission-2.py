class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i):
            #base case
            if sum(comb) == target:
                res.append(comb.copy())
                return
            elif sum(comb) > target:
                return
            
            for j in range(i, len(nums)):
                comb.append(nums[j])
                dfs(j)
                comb.pop()
        dfs(0)
        return res
                