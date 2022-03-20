class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = set()
        
        def backtrack(val = target, curr = [], start = 0):
            if val <= 0:
                if val == 0:
                    ret.add(tuple(sorted(curr[:])))
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(val - candidates[i], curr, i)
                curr.pop()
        
        backtrack()
        
        return ret
                    