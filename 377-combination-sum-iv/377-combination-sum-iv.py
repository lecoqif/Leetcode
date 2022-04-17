class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def backtrack(remain: int) -> None:
            if remain == 0:
                return 1
            
            result = 0
            
            for i in nums:
                if remain - i >= 0:
                    result += backtrack(remain - i)
            
            return result
            
            
        return backtrack(target)