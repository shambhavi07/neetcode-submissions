class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])
        # visited=set()
        max_area=0
        
        def dfs(r,c):
            # if (r,c) in visited:
            #     return

            if r<0 or r> ROWS-1 or c<0 or c>COLS-1 or grid[r][c]==0:
                return 0

            # switch the cell to 0 
            grid[r][c] = 0
            
            return 1+ dfs(r+1, c) + dfs(r-1,c) + dfs(r, c+1)+ dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    max_area= max(max_area, dfs(r,c))
        return max_area
                    
                
        