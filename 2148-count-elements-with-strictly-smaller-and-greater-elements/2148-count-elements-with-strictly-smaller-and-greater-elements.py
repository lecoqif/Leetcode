class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        nums.sort()
        
        minNum, maxNum = nums[0], nums[-1]
        ret = 0
        
        for num in nums[1:-1]:
            if num > minNum and num < maxNum:
                ret += 1
        
        return ret
                