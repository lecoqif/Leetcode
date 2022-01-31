class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def find_pivot(nums):
            
            start, end = 0, len(nums) - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] >= nums[0]:
                    start = mid + 1
                
                elif nums[mid] < nums[0] and nums[mid] < nums[mid - 1]:
                        return mid
                
                else:
                    end = mid - 1
            
        pivot = 0 if nums[0] < nums[len(nums) - 1] else find_pivot(nums)
        
        return nums[pivot]
        
                    
        