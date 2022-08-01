class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Fuck you Orest
        if m == 0 or n == 0: return 0
        
        ans = 0
        dp = [[1 for _ in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
                