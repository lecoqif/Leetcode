class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ret = []
        
        def backtrack(curr: List[int], target: int, k: int, start: int):
            
            if target == 0 and k == 0:
                ret.append(curr)
                return
            
            if k < 0:
                return
            
            for i in range(start, 10):
                if target - i < 0:
                    break
                
                curr.append(i)
                backtrack(curr[:], target - i, k - 1, i + 1)
                curr.pop()
            
        backtrack([], n, k, 1)
        
        return ret