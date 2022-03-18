class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        ret = deque()
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                ret.appendleft(nums[left] ** 2)
                left += 1
            
            else:
                ret.appendleft(nums[right] ** 2)
                right -= 1
        
        return list(ret)
            
            
                