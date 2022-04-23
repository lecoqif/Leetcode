class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSums = defaultdict(int)
        
        ret = 0
        curr = 0
        
        for i, val in enumerate(nums):
            curr += val
            
            if curr == k:
                ret += 1
            
            ret += prefixSums[curr - k]
            
            prefixSums[curr] += 1
        
        return ret
        
        