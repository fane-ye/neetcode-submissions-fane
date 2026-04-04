from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        window = []
        res = []
        
        for i in range(len(arr)):
            # Add current element to window
            window.append(arr[i])
            
            # If window has exactly k elements
            if len(window) == k:
                # First window becomes our initial best
                if not res:
                    res = window.copy()
                else:
                    # Compare current window with best window
                    # Compare the elements that differ between windows
                    # (the leftmost element of each window)
                    if abs(window[-1] - x) < abs(res[0] - x):
                        # Current window is better
                        res = window.copy()
                    elif abs(window[-1] - x) == abs(res[0] - x):
                        # If distances are equal, check if current window
                        # has smaller leftmost element
                        if window[0] < res[0]:
                            res = window.copy()
                
                # Slide window by removing leftmost element
                window.pop(0)
        
        return res