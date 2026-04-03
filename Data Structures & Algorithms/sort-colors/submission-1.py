class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #have array of size k
        #iterate through n elements of array
        #if nums[i], add count
        count_arr = [0, 0, 0] #red(0), white(1), blue(2)
        for i in range(len(nums)):
            count_arr[nums[i]] += 1


        
        #once done, iterate through size k array, and overwrite originl nums
        n = 0
        for color in range(len(count_arr)): 
            for k in range(count_arr[color]): #number of times the element appears
                nums[n] = color
                n += 1
        return
