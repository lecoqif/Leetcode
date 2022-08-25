class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        maxNum, minNum = float('-inf'), float('inf')
        
        for num in nums:
            maxNum = max(maxNum, num)
            minNum = min(minNum, num)
        
        ret = 0
        
        for num in nums:
            if num < maxNum and num > minNum:
                ret += 1
        
        return ret
                