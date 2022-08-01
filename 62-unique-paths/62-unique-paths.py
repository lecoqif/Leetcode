class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0:
            return 0
        
        ans = 0
        
        dp = [[0 for _ in range(n)] for i in range(m)]
        
        dp[0][0] = 1
        
        def grid_val(row: int, col: int) -> int:
            if not (0 <= row < m and 0 <= col < n):
                return 0
            
            return dp[row][col]
        
        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0: 
                    continue
                    
                dp[i][j] = grid_val(i - 1, j) + grid_val(i, j - 1)
        
        return dp[m - 1][n - 1]
                