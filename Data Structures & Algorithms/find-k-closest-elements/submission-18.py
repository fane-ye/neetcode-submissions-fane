class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = None

        window = deque()
        for r in range(len(arr)):
            window.append(arr[r])
            if len(window) == k:
                if not res:
                    res = list(window)

                #if current window sum of distances is smaller than res update
                elif abs(res[0] - x) > abs(window[-1] - x):
                    res = list(window)
                window.popleft()
        
        return res