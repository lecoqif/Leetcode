import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        
        pq = [(-value, key) for key, value in c.items()]
        
        heapq.heapify(pq)
        
        prev_freq, prev_char = 0, ''
        
        res = ''
        
        while pq:
            freq, char = heapq.heappop(pq)
            res += char
            freq += 1
            
            if prev_freq < 0:
                heapq.heappush(pq, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq, char
        
        return res if len(res) == len(S) else ''
            