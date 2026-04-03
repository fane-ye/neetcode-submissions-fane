class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue

                # check if val alrdy exists in that row, col, sqr
                elif val in rows[r] or val in cols[c] or val in sqrs[(r // 3, c // 3)]:
                    return False

                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    sqrs[(r // 3, c // 3)].add(val)
        
        return True