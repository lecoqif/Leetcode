class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(start: int, remain: int) -> int:
            if start == len(nums) and remain == 0:
                return 1
            
            elif start == len(nums) and remain != 0:
                return 0
            
            result = 0
            
            result += dfs(start + 1, remain - nums[start])
            result += dfs(start + 1, remain + nums[start])
            
            return result
        
        return dfs(0, target)