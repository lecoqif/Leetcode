class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0:
            return 0
        
        ans = 0
        
        dp = [[1 for _ in range(n)] for i in range(m)]
        
#         dp[0][0] = 1
        
#         def grid_val(row: int, col: int) -> int:
#             if not (0 <= row < m and 0 <= col < n):
#                 return 0
            
#             return dp[row][col]
        
        for i in range(1, m):
            for j in range(1, n):

                # if i == 0 and j == 0: 
                #     continue
                    
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
                