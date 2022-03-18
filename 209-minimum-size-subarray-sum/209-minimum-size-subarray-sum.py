class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        curr_sum = 0
        ret = float('inf')
        
        while right < n:
            curr_sum += nums[right]
            
            
            while curr_sum >= target:
                ret = min(ret, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
            right += 1
            
        return ret if ret != float('inf') else 0
            
            
        
            
            