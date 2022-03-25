class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        
        if n < 3:
            return []
        
        nums.sort()
        
        ret = []
        
        for i, val in enumerate(nums):
            
            start, end = i + 1, n - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while start < end:
                
                total = nums[i] + nums[start] + nums[end]
                
                if total == 0:
                    ret.append(nums[a] for a in [i, start, end])
                    start += 1
                    end -= 1
                
                    while start + 1 < n - 1 and nums[start] == nums[start - 1]:
                        start += 1
                
                elif total < 0:
                    start += 1
                    
                else:
                    end -= 1
                    
        return ret
                