class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time complexity: O(1)
        # Space: O(1) fixed size board
        # rows= defaultdict(set)
        # cols= defaultdict(set)
        # boxes = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         value= board[r][c] 
        #         if value == ".":
        #             continue
                
        #         # box id needed for boxes dict {set}
        #         # boxId -> {val1,val2...}
        #         # we are only dealing with positive nums inn the board
        #         boxId= (r//3, c//3)

        #         if value in rows[r]:
        #             return False
        #         if value in cols[c]:
        #             return False
        #         if value in boxes[boxId]:
        #             return False
                
        #         # if no duplicate in any we add to the dicts
        #         # return True, sudoko is valid
        #         # For dictionary rows with key add val to its values set
        #         rows[r].add(value)
        #         cols[c].add(value)
        #         boxes[boxId].add(value)

        # return True

        # approach 2: bitmask
        # We need list with 9 spots
        row_mask= [0]*9
        col_mask= [0]*9
        box_mask= [0]*9

        for r in range(9):
            for c in range(9):
                value= board[r][c]
                if value == ".":
                    continue
                digit= int(value)
                bit= 1 << (digit-1)
                boxId= (r//3)*3 + (c//3) # for each box 0-9
                #  # nonzero = truthy = duplicate found
                if (row_mask[r] & bit) or (col_mask[c] & bit) or (box_mask[boxId] & bit):
                    return False
                
                # bitis 0 so update it to 1
                row_mask[r] |= bit
                col_mask[c] |= bit
                box_mask[boxId] |= bit
        return True

        