class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find_pivot(nums):
            start, end = 0, len(nums) - 1
            
            pivot = 0
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if nums[mid] < nums[0]:
                    end = mid - 1
                    pivot = mid
                
                else:
                    start = mid + 1
            
            return pivot
        
        pivot = find_pivot(nums)
        
        return nums[pivot]