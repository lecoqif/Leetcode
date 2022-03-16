class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        for i, val in enumerate(nums[1:]):
            if val == nums[i]:
                return val
        
        return -1
            