class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        
        graph = defaultdict(list)
        
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        visited = set()
        
        q = deque(list(range(n)))
        
        def dfs(node: int) -> None:
            
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor)
        
        while q:
            curr = q.popleft()
            
            if curr in visited:
                continue
            
            count += 1
            
            dfs(curr)
        
        return count