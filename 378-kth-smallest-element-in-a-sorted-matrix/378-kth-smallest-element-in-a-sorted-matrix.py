from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for i in range(ROWS):
            print(i * COLS)
            heappush(heap, (matrix[i][0], i, 0))
        
        i = 0
        
        while i < k - 1:
            _, row, col = heappop(heap)
            
            if col < COLS - 1:
                heappush(heap, (matrix[row][col + 1], row, col + 1))
            
            i += 1
        
        ret, _, _ = heappop(heap)
        return ret
                