class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m * n != len(original):
            return []
        
        ret = [[0 for _ in range(n)] for i in range(m)]
        
        for i, val in enumerate(original):
            row = i // n
            col = i % n
            
            ret[row][col] = val
        
        return ret