class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)
        
        ans = 0
        
        while r < n:
            if nums[r] == 0:
                ans += r - l + 1
            
            else:
                l = r + 1
            
            r += 1
        
        return ans
                
            
        
        