class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        # [maxlen, count]
        dp = [[1, 1] for _ in range(len(nums))]
        
        maxLisLen = 0
        
        for i, num in enumerate(nums):
            maxlen, count = dp[i]
            
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > maxlen:
                        maxlen, count = dp[j][0] + 1, dp[j][1]
                    
                    elif dp[j][0] + 1 == maxlen:
                        count += dp[j][1]
            
            dp[i] = [maxlen, count]
            
            maxLisLen = max(maxlen, maxLisLen)
            
        return sum([item[1] for item in dp if item[0] == maxLisLen])