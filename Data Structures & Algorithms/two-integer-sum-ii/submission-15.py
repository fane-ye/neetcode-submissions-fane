class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = numbers
        n = len(numbers)
        seen = {}

        
        for i in range(n):
            need = target - arr[i]
            if need in seen:
                return [seen[need] + 1, i + 1]
            seen[arr[i]] = i
        

        