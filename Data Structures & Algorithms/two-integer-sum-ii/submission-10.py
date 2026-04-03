class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = numbers
        n = len(numbers)
        pos = {}
        for i in range(n):
            pos[arr[i]] = i

        
        for i in range(n):
            need = target - arr[i]
            if need in pos:
                return [i + 1, pos[need] + 1]
        

        