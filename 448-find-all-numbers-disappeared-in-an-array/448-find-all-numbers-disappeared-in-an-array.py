class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        
        n = len(nums)
        
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
        
        for i in range(n):
            if nums[i] > 0:
                ret.append(i + 1)
        
        return ret