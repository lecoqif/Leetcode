class Solution:
    def tribonacci(self, n: int) -> int:
        
        trib = [0, 1, 1]
        
        if n <= 2: return trib[n]
        
        for i in range(3, n + 1):
            trib.append(sum(trib[-3:]))
        
        return trib[n]