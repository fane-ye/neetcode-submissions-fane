class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)
        #calculate rows
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".": 
                    continue
                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                sqr = (i // 3, j // 3)
                if num in sqrs[sqr]:
                    return False
                sqrs[sqr].add(num)

        return True


            

        