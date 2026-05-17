class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TRICK: CHECK FOR EACH ROW
        rows, cols = len(matrix), len(matrix[0])
        # for each row compare with target
        for row in range(rows):
            if matrix[row][cols-1] == target:
                return True
            elif matrix[row][cols-1] > target:
                left, right= 0, cols-1
                while left <=right:
                    mid= left + (right-left)//2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        left = mid +1
                    else:
                        right = mid-1
                return False
        return False

        # TRICK: FLATTEN THE MATRIX TO 1D
        # row, cols length need for converting back to 2D matrix index
        # `matrix[0]` is just the first row. Its length is the number of columns. That's it.
        # rows, cols= len(matrix), len(matrix[0])
        # # left right pointers for the binary search
        # # also it converts the matrix to 1D
        # # This is the "pretend it's a flat 1D array" trick. A 3×4 matrix has 12 elements total. If it were a flat list, indices would run from 0 to 11.
        # # So `right = rows * cols - 1 = 3*4 - 1 = 11`. Just the last index of that imaginary flat array.
        # left, right= 0, rows * cols -1

        # while left <= right:
        #     mid = left + (right - left) //2
        #     # index back to 2D matrix
        #     val= matrix[mid // cols][mid % cols]

        #     if val == target:
        #         return True
        #     elif val < target:
        #         left = mid +1
        #     else:
        #         right = mid -1
        # return False 

        