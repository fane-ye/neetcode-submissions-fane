class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row validity
        square_sets = [set() for i in range(9)]
        for i in range(9):
            row = board[i]
            row_set = set()
            for num in row:
                if num in row_set:
                    return False
                elif num != ".":
                    row_set.add(num)
            
            col_set = set()
            for j in range(9): #cols
                num = board[j][i]
                if num in col_set:
                    return False
                elif num != ".":
                    col_set.add(num)

                square_index = int(j // 3) + 3 * int(i // 3)
                num_sqr = board[i][j]
                sqr_set = square_sets[square_index]
                if num_sqr in sqr_set:
                    return False
                elif num_sqr != ".":
                    sqr_set.add(num_sqr)
        return True