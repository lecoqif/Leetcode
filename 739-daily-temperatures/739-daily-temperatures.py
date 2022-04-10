class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        
        n = len(T)
        
        res = [0] * n
        
        for i in range(n - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
                
            res[i] = stack[-1] - i if stack else 0
            
            stack.append(i)
        
        return res