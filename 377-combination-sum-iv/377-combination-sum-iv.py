class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def backtrack(curr: int) -> int:
            
            if curr == 0:
                return 1
            
            count = 0
            
            for i in nums:
                if curr - i >= 0: count += backtrack(curr - i)
                
            return count
        
        return backtrack(target)
            

                