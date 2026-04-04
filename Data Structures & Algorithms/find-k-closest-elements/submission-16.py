class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize window with first k elements
        window = arr[:k]
        
        # Slide the window from left to right
        for i in range(k, len(arr)):
            # Compare the element leaving vs the element entering
            leaving = arr[i - k]  # Leftmost element of current window
            entering = arr[i]     # New element to add
            
            # If the new element is closer than the leaving element,
            # update the window
            if abs(entering - x) < abs(leaving - x):
                window = window[1:] + [entering]
    
        return window