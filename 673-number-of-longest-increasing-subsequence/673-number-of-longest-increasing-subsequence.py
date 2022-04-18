class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # [maxlen, count] for every index
        dp = [ [1, 1] for _ in range(n) ]
        
        # max length of LIS
        maxLisLen = 0
        
        for i in range(n):
            maxlen, count = dp[i]
            
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 == maxlen:
                        count += dp[j][1]
                    
                    elif dp[j][0] + 1 > maxlen:
                        maxlen, count = dp[j][0] + 1, dp[j][1]
            
            dp[i] = [maxlen, count]
            
            maxLisLen = max(maxLisLen, maxlen)
        
        return sum([item[1] for item in dp if item[0] == maxLisLen])
            
            
        