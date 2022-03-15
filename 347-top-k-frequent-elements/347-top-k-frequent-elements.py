from collections import defaultdict, Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        
        heap = []
        
        for key in hm.keys():
            heappush(heap, (-hm[key], key))
        
        ret = [heappop(heap)[1] for i in range(k)]
        
        return ret
        

            
        