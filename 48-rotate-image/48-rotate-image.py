class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for row in range(ROWS // 2):
            for col in range(row, ROWS - 1 - row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[COLS - 1 - col][row]
                matrix[COLS - 1 - col][row] = matrix[ROWS - 1 - row][COLS - 1 - col]
                matrix[ROWS - 1 - row][COLS - 1 - col] = matrix[col][ROWS - 1 - row]
                matrix[col][ROWS - 1 - row] = temp
                

                
            
        