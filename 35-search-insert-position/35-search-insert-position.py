class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        ret = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= target:
                ret = mid
                start = mid + 1
            
            else:
                end = mid - 1
        
        return ret + 1
                