class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isCol = False
        R, C = len(matrix), len(matrix[0])
        
        for i in range(len(matrix)):
            
            if matrix[i][0] == 0:
                isCol = True
            
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            matrix[0] = [0] * C
        
        if isCol:
            for i in range(R):
                matrix[i][0] = 0