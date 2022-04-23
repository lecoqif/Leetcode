class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        paths = []

        q = deque()
        
        q.append((0, []))
        
        while q:
            node, path = q.popleft()
            
            path.append(node)
            if node == n - 1:
                paths.append(path)
                continue
            
            
            
            for nei in graph[node]:
                q.append((nei, path[:]))
        
        return paths
            
        
        