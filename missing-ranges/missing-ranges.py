class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if upper - lower == 0:
                return [str(lower)]
            
            else:
                return [str(lower) + "->" + str(upper)]
            
            
        ret = []
        
        prev = lower - 1
        
        nums.append(upper + 1)
        
        for num in nums:
            if num - prev > 1:
                if num - prev == 2:
                    ret.append(str(prev + 1))
                
                else:
                    ret.append(str(prev + 1) + "->" + str(num - 1))
            
            prev = num
        
        return ret