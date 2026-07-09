class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])
        visited= set()
        count=0
        
        # inner loop for each cell in the row
        def dfs(r,c):
            # check that decides to stop and not process further
            # visited memebership, check coordinates
            if (r,c) in visited:
                return

            # out of bound check first to skip itr then check is island or not
            if r<0 or r>ROWS-1 or c<0 or c>COLS-1 or grid[r][c]=='0':
                return

            visited.add((r,c))
            # up
            dfs(r-1,c)
            # down
            dfs(r+1,c)
            # left
            dfs(r,c-1)
            # right
            dfs(r,c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count+=1
                    dfs(r,c)
        return count