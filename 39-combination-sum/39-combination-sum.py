class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = set()
        
        def backtrack(val = target, curr = []):
            if val <= 0:
                if val == 0:
                    ret.add(tuple(sorted(curr[:])))
                return
            
            for i in candidates:
                val -= i
                curr.append(i)
                backtrack(val, curr)
                curr.pop()
                val += i
        
        backtrack()
        
        return ret
                    