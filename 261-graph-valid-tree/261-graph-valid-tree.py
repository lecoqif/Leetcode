from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        seen = set()
        
        q = deque()
        
        q.append((0, -1))
        
        while q:
            curr, parent = q.popleft()
            seen.add(curr)
            
            for nei in graph[curr]:
                if nei != parent:
                    if nei in seen:
                        return False
                    
                    q.append((nei, curr))
        
        return len(seen) == n
                
        
        