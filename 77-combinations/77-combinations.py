
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        
        def backtrack(curr: List[int], start: int, k: int) -> None:
            
            if k == 0:
                ret.append(curr)
                return
            
            for i in range(start, n + 1):
                curr.append(i)
                backtrack(curr[:], i + 1, k - 1)
                curr.pop()
        
        backtrack([], 1, k)
        
        return ret