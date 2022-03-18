class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            left = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
            
            if nums[mid] > left and nums[mid] > right:
                return mid
            
            if nums[mid] < left:
                end = mid - 1
            
            elif nums[mid] < right:
                start = mid + 1
        