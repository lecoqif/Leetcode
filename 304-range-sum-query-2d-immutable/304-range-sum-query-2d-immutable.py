class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.dp = [[0 for _ in range(self.COLS)] for i in range(self.ROWS)]
        self.fill_dp()
        
    def fill_dp(self):
        self.dp[0][0] = self.matrix[0][0]
        for j in range(1, self.COLS):
            self.dp[0][j] = self.dp[0][j - 1] + self.matrix[0][j]
        
        for i in range(1, self.ROWS):
            self.dp[i][0] = self.dp[i - 1][0] + self.matrix[i][0]
        
        for i in range(1, self.ROWS):
            for j in range(1, self.COLS):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1] + self.matrix[i][j]
    
    def sumFromOrigin(self, row: int, col: int) -> int:
        if row < 0 or col < 0:
            return 0
        
        return self.dp[row][col]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        leftRect = self.sumFromOrigin(row2, col1 - 1) 
        upperRect = self.sumFromOrigin(row1 - 1, col2)
        remainder = self.sumFromOrigin(row1 - 1, col1 - 1)
        total = self.sumFromOrigin(row2, col2)
        
        return total - leftRect - upperRect + remainder
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)