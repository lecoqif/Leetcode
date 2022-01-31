class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i, val in enumerate(nums):
            for j in range(i):
                if val > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)