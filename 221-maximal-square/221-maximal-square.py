class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = [[0 for _ in range(COLS)] for i in range(ROWS)]
        
        res = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    res = 1
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if dp[i][j]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        
        return res ** 2
        
        
                    