class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        
        for i, val in enumerate(nums):
            if nums[abs(val) - 1] < 0:
                ret.append(abs(val))
            
            else:
                nums[abs(val) - 1] = -1 * nums[abs(val) - 1]
        
        return ret