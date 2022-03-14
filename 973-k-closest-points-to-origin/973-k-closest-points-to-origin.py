from heapq import heappush, heappop
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            dist = self.euclideanDistance(point)
            heappush(heap, (-dist, point))
            if len(heap) > K:
                heappop(heap)
        
        ret = list(map(lambda x:x[1], heap))
        
        return ret
        
    def euclideanDistance(self, point: List[int]) -> float:
        dist = (point[0]) ** 2 + (point[1]) ** 2
        return sqrt(dist)
        
        