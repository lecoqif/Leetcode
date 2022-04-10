class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n
        
        for i in range(n * 2 - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            res[i % n] = stack[-1] if stack else -1
            
            stack.append(nums[i % n])
        
        return res
        
        