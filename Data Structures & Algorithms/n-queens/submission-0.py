class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # what we return list of strings for final board
        result=[]
        cols= set() #set because membership check-use col only once
        diag1= set()
        diag2= set()
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            if row ==n:
                #  convert board to list of strings, collect a COPY
                snap= ["".join(r) for r in board]
                result.append(snap)
                return

            # recirse into cols for each row
            for col in range(n):
                # prine invalid ans
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                
                # choose
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row +col)

                # explore next row
                backtrack(row+1)
                # unchoose 
                board[row][col]="."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result

        