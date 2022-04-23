class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph) - 1
        
        @lru_cache(None)
        def allPathsToTarget(node = 0) -> List[List[int]]:
            if node == target:
                return [[node]]
            
            results = [] 
            
            for nei in graph[node]:
                for path in allPathsToTarget(nei):
                    results.append([node] + path)
            
            return results
        
        return allPathsToTarget()
            
        
        