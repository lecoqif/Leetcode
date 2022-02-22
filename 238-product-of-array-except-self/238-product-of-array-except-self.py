class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        left = [0 for _ in range(n)]
        
        left[0] = 1
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        right = nums[n - 1]
        
        for i in range(n - 2, -1, -1):
            left[i] *= right
            right *= nums[i]
        
        return left
            
        
        
        