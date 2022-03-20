from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        
        def backtrack(st = 1, curr=[]):
            if len(curr) == k:
                ret.append(curr[:])
                return
            
            for i in range(st, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack()
        
        return ret
                