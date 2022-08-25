class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        maxNum, minNum, ret = max(nums), min(nums), 0
        
        for num in nums:
            if num < maxNum and num > minNum:
                ret += 1
        
        return ret
                
        
        
        
        