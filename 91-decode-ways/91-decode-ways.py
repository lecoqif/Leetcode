class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1
        
        for i in range(1, len(dp)):
            if 0 < int(s[i - 1]):
                dp[i] = dp[i - 1]
            
            if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[len(s)]
            
            