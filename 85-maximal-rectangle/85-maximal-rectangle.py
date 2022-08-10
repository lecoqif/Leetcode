class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = [[(0, 0, 0, 0, 0) for _ in range(COLS)] for j in range(ROWS)]
        res = 0
        
        # (val, up, left, min lefts of up)
        if matrix[0][0] == "1":
            dp[0][0] = (1, 1, 1) 
            res = 1
        
        for i in range(1, ROWS):
            if matrix[i][0] == "1":
                val = dp[i - 1][0]
                dp[i][0] = (val[0] + 1, val[1] + 1, 1)
                res = max(res, dp[i][0][0])
        
        for j in range(1, COLS):
            if matrix[0][j] == "1":
                val = dp[0][j - 1]
                dp[0][j] = (val[0] + 1, 1, val[2] + 1)
                res = max(res, dp[0][j][0])
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == "1":
                    up = dp[i - 1][j][1] + 1
                    left = dp[i][j - 1][2] + 1
                    val = 0
                    temp = left
                    for k in range(up - 1):
                        temp = min(temp, dp[i - 1 - k][j][2])
                        val = max(val, (k + 2) * temp)
                    dp[i][j] = (max(val, left, up), up, left)
                    temp = dp[i][j]
                    res = max(res, dp[i][j][0])
        
        return res
                    
                    
        
        
        
        
            
            