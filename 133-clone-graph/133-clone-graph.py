"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        graph = {}
        visited = set()
        
        q = deque()
        
        q.append(node)
        
        while q:
            curr = q.popleft()
            
            visited.add(curr.val)
            
            graph[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                if nei.val not in visited:
                    q.append(nei)
            
        for vertex in graph:
            for nei in vertex.neighbors:
                graph[vertex].neighbors.append(graph[nei])
        
        return graph[node]
        