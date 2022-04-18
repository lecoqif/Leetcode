class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [ float('inf') for _ in range(n) ]
        
        dp[n - 1] = 0
        
        for i in range(n - 2, -1, -1):
            minJumps = dp[i]
            
            for j in range(i + 1, n):
                if i + nums[i] >= j:
                    minJumps = min(minJumps, dp[j] + 1)
                
                if i + nums[i] < j:
                    break
            
            dp[i] = minJumps
        
        print(dp)
        return dp[0]
                    
            
        
        