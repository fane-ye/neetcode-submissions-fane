class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        index = -1
        while lo <= hi:
            mid = (lo + hi)//2
            mid_l = matrix[mid][0]
            mid_r = matrix[mid][-1]
            #if target in mid range
            if mid_l <= target <= mid_r:
                #search in the range
                index = self.b_search(matrix[mid], target)
                break
            #if target in lo range
            elif target < mid_l:
                hi = mid - 1
            #if target in hi range
            elif target > mid_r:
                lo = mid + 1
            

        if index != -1:
            return True

        return False
    def b_search(self, arr, target):
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = (lo + hi)//2

            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                hi = mid - 1
            elif target > arr[mid]:
                lo = mid + 1
        else:
            return -1





        