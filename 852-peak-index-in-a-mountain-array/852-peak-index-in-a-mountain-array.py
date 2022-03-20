class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        def gold1(l, r):
            return l + int(round((r - l) * 0.382))
        
        def gold2(l, r):
            return l + int(round((r - l) * 0.618))
        
        start, end = 0, len(A) - 1
        
        x1, x2 = gold1(start, end), gold2(start, end)

        while x1 < x2:
            if A[x1] < A[x2]:
                start = x1
                x1 = x2
                x2 = gold2(start, end)
            
            else:
                end = x2
                x2 = x1
                x1 = gold1(start, end)
        
        return A.index(max(A[start:end + 1]), start)
           