class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS= len(grid), len(grid[0])
        q= deque()

        # update the queue with all entry ponts i.e
        # grid[r][c]==0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]== 0:
                    q.append((r,c))

        # BFS Loop to update shortest distance
        directions= [(-1,0),(1,0),(0,-1),(0,1)]
        # go until queue is empty that is all gates are processed
        while q:
            row, col= q.popleft()
            # check each direction for each gate
            for dr, dc in directions:
                nr, nc= row +dr, col+dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc]== 2147483647:
                    # write the actual distance
                    grid[nr][nc]= grid[row][col] + 1
                    q.append((nr, nc))

        