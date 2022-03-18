class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        row, col = 0, COLS - 1
        
        while col >= 0 and row < ROWS:
            val = matrix[row][col]
            
            if val == target:
                return True
            
            if val < target:
                row += 1
            
            if val > target:
                col -= 1
        
        return False
        