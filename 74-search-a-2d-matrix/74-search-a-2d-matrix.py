class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        
        COLS = len(matrix[0])
        
        row, col = 0, COLS - 1
        
        while row < ROWS and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            
            if val < target:
                row += 1
            
            if val > target:
                col -= 1
        
        return False
            
            
            