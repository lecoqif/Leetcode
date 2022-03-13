from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        
        q = deque([start])
        
        while len(q) > 0:
            curr = q.popleft()
            
            if arr[curr] == 0:
                return True
            
            visited.add(curr)
            
            for val in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= val < len(arr) and val not in visited:
                    q.append(val)
            
        return False
            
            