class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1: return 0
        
        left = right = ret = 0
        
        n = len(nums)
        
        currProduct = 1
        
        while right < n:
            currProduct *= nums[right]
            right += 1
            
            while currProduct >= k:
                currProduct /= nums[left]
                left += 1
            
            ret += right - left
        
        return ret
                
            
            
            
            
            
            
        