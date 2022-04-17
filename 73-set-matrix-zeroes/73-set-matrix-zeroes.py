class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        rows = [0] * ROWS
        cols = [0] * COLS

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        
        for i in range(ROWS):
            if rows[i] == 1:
                for j in range(COLS):
                    matrix[i][j] = 0
        
        for i in range(COLS):
            if cols[i] == 1:
                for j in range(ROWS):
                    matrix[j][i] = 0
            
        