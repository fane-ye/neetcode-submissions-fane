class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #calculate rows
        for row in board:
            nums = set()
            for num in row:
                if num == ".": 
                    continue
                if num in nums:
                    return False
                nums.add(num)

        #cols
        for i in range(9):
            nums = set()
            for j in range(9):
                num = board[j][i]
                if num == ".": 
                    continue
                if num in nums:
                    return False
                nums.add(num)


        #squares
        for sqr in range(0, 9, 3):
            for base in range(0, 9, 3):
                nums = set()
                for i in range(3):
                    for j in range(3):
                        row = sqr  + i
                        col = base + j
                        num = board[row][col]
                        if num == ".": 
                            continue
                        if num in nums:
                            return False
                        nums.add(num)

        return True


            

        