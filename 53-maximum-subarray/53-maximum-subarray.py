class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_now = max_total = nums[0]
        
        for i in range(1, len(nums)):
            max_now = max(max_now + nums[i], nums[i])
            max_total = max(max_total, max_now)
            
        return max_total