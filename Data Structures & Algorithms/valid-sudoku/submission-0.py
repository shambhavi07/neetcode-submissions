class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)
        cols= defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value= board[r][c] 
                if value == ".":
                    continue
                
                # box id needed for boxes dict {set}
                # boxId -> {val1,val2...}
                # we are only dealing with positive nums inn the board
                boxId= (r//3, c//3)

                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[boxId]:
                    return False
                
                # if no duplicate in any we add to the dicts
                # return True, sudoko is valid
                # For dictionary rows with key add val to its values set
                rows[r].add(value)
                cols[c].add(value)
                boxes[boxId].add(value)

        return True

        