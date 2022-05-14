from heapq import heappop, heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for i in range(ROWS):
            heappush(heap, (matrix[i][0], i, 0))
        
        for i in range(k - 1):
            _, x, y = heappop(heap)
            if y < COLS - 1:
                heappush(heap, (matrix[x][y + 1], x, y + 1))
        
        return heappop(heap)[0]
            