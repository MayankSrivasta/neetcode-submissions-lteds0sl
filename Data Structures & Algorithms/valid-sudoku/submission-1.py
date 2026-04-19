class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squ = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]

                if v == '.':
                    continue
                
                if (v in row[r] or v in col[c] or 
                v in squ[(r //3, c // 3)]):
                    return False

                row[r].add(v)
                col[c].add(v)
                squ[(r // 3, c // 3)].add(v)
            
        return True