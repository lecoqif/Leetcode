class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1: return nums[0]
        
        if n == 2: return max(nums)
        
        dp = [0 for _ in range(n)]
        
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[n - 1]
            