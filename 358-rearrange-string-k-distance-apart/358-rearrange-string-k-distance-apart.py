from collections import Counter, defaultdict
from heapq import heappush, heappop
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        if k == 0: return s
        
        counter = Counter(s)
        heap = []
        
        for ch in counter:
            heappush(heap, (-counter[ch], ch, counter[ch]))
        
        ret = ""
        
        idx, hm = 0, defaultdict(list)
        
        while idx < len(s):
            
            if not heap: return ""
            
            _, ch, count = heappop(heap)
            ret += ch
            
            if count > 1: hm[idx + k].append((ch, count - 1))
                
            idx += 1
            
            if idx in hm:
                for ch, count in hm[idx]:
                    heappush(heap, (-count, ch, count))
            
             
        
        return ret if len(ret) == len(s) else ""
            
            