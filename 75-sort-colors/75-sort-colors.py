class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = curr = 0
        right = n - 1
        
        while curr <= right:
            if nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            
            elif nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                curr += 1
                left += 1
            
            else:
                curr += 1
        
        