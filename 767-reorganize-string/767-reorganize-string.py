from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # Frequency counts
        counter = Counter(s)
        
        heap = []
        
        for letter in counter:
            heappush(heap, (-counter[letter], letter))
        
        ret = ""
        
        prev_char, prev_count = '', 0
        
        while heap:
            curr_count, curr_char = heappop(heap)
            ret += curr_char
            
            if prev_count < 0:
                heappush(heap, (prev_count, prev_char))
            
            prev_char, prev_count = curr_char, curr_count + 1
        
        return ret if len(ret) == len(s) else ""
        