class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        curr_sum, left_sum, n = sum(nums), 0, len(nums)
        
        for i, num in enumerate(nums):
            curr_sum -= num
            
            if curr_sum == left_sum:
                return i
            
            left_sum += num
        
        return -1
            