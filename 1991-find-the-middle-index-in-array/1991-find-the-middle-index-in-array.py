class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        curr_sum, left_sum, n = 0, 0, len(nums)
        
        for i in range(n - 1, -1, -1):
            curr_sum += nums[i]
        
        for i, num in enumerate(nums):
            curr_sum -= num
            
            if curr_sum == left_sum:
                return i
            
            left_sum += num
        
        return -1
            