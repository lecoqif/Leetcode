class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        
        n = len(nums)
        
        seen = set([i for i in range(1, n + 1)])
        
        for i in nums:
            if i in seen:
                seen.remove(i)
        
        return list(seen)