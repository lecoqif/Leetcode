class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        flag = False
        
        for i in nums:
            if i == 1:
                flag = True
        
        if not flag:
            return 1
        
        n = len(nums)
        
        for i, val in enumerate(nums):
            if val <= 0 or val > n:
                nums[i] = 1
        
        for i, val in enumerate(nums):
            abs_val = abs(nums[i]) - 1
            nums[abs_val] = -1 * nums[abs_val] if nums[abs_val] > 0 else nums[abs_val]
            
        for i, val in enumerate(nums):
            if val > 0:
                return i + 1
        
        return n + 1