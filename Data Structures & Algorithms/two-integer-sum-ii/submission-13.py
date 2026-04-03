class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = numbers
        n = len(numbers)
        pos = {}

        
        for i in range(n):
            need = target - arr[i]
            if need in pos:
                return [pos[need] + 1, i + 1]
            pos[arr[i]] = i
        

        