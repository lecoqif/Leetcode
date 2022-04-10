class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr: List[int]):
            if len(curr) == len(nums):
                output.append(curr[:])
            
            for i in nums:
                if i in curr:
                    continue
                
                curr.append(i)
                backtrack(curr)
                curr.pop()
            
        
        output = []
        
        for i in nums:
            backtrack([i])
        
        return output