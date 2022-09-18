import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        
        ret = 1
        
        heapq.heappush(heap, intervals[0][1])
        
        for interval in intervals[1:]:
            top_end = heap[0]
            
            if interval[0] > top_end:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval[1])
            
            ret = max(ret, len(heap))
        
        return ret
                
            
            
            
        