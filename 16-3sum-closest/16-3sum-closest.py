class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        
        nums.sort()
        
        n = len(nums)
        
        ret = 0
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            start, end = i + 1, n - 1
            
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                newDiff = abs(total - target)
                
                if newDiff < diff:
                    ret = total
                    diff = newDiff
                
                if total == target:
                    return total
                
                if total < target:
                    start += 1
                
                else:
                    end -= 1
        
        return ret
                    
                