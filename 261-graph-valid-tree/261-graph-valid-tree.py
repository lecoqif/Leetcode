class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        seen = set()
        
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        
        q = deque()
        q.append((-1, 0))
        
        while q:
            parent, curr = q.popleft()
            
            if curr in seen:
                return False
            
            seen.add(curr)
            
            for nei in graph[curr]:
                if nei != parent:
                    q.append((curr, nei))
        
        return len(seen) == n
                
            
            