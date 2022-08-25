class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        maxNum, minNum = max(nums), min(nums)

        ret = 0
        
        for num in nums:
            if num < maxNum and num > minNum:
                ret += 1
        
        return ret
                