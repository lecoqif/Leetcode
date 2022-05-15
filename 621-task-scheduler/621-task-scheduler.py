from collections import Counter, defaultdict
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0: return len(tasks)
        
        counter = Counter(tasks)
        
        
        
        heap = []
        
        for task, count in counter.items():
            heappush(heap, (-count, task, count))
        
        hm = {}
        
        ret = 0
        
        while hm or heap:
            ret += 1
            
            if heap:
                _, task, count = heappop(heap)
                if count > 1: hm[ret + n] = (task, count - 1)
            
            if ret in hm:
                task, count = hm[ret]
                heappush(heap, (-count, task, count))
                del hm[ret]
        
        return ret
            
            
            
            
        
        