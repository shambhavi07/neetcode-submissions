class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS= len(board), len(board[0])

        def dfs(r,c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            if board[r][c] == 'X' or board[r][c] == 'S':
                return

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            
            board[r][c]= 'S'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # top and bottom row
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)

        # left and right cols
        for r in range(ROWS):
            dfs(r,0)
            dfs(r, COLS-1)

        # Pass 2 + 3 combined: flip trapped, restore safe
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'



            

            
            
         