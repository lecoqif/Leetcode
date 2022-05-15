from collections import Counter, defaultdict
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        
        maxf = max(counter.values())
        
        if n == 0 or maxf == 1: return len(tasks)

        
        
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
            
            
            
            
        
        