from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        def euclidean_distance(x, y):
            return math.sqrt(x ** 2 + y ** 2)
        
        for x, y in points:
            dist = euclidean_distance(x, y)
            heappush(heap, (-dist, [x, y]))
            
            if len(heap) > k:
                heappop(heap)
        
        return [x[1] for x in heap]