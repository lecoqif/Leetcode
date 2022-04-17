class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def houseRob(nums: List[int]) -> int:
            if len(nums) <= 2:
                return max(nums)
            
            dp = [ nums[0], max(nums[0], nums[1]) ]
            
            for i in range(2, len(nums)):
                dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
            
            return dp[len(nums) - 1]
        
        return max(houseRob(nums[:len(nums) - 1]), houseRob(nums[1:]))