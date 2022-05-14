from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        seen = set()
        
        count = 0
        
        def dfs(vertex: int) -> None:
            seen.add(vertex)
            
            for nei in graph[vertex]:
                if nei not in seen:
                    dfs(nei)
        
        for v in range(n):
            if v not in seen:
                count += 1
                dfs(v)
        
        return count