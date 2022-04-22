class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        dp = [0 for _ in range(n)]
        
        for pos, reach in lights:
            start = max(0, pos - reach)
            end = min(n - 1, pos + reach) + 1
            
            dp[start] += 1
            
            if end < n:
                dp[end] -= 1
        
        ret = 0
        
        for i, val in enumerate(dp):
            if i > 0: 
                dp[i] += dp[i - 1]
            
            if dp[i] >= requirement[i]:
                ret += 1
        
        return ret
            
            