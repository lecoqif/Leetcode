"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph = {}
        visited = set()
        
        if not node:
            return None
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            graph[node] = Node(node.val)
            for neighbor in node.neighbors:
                dfs(neighbor)
        
        dfs(node)
        
        for val in graph:
            new_node = graph[val]
            
            for neighbor in val.neighbors:
                new_node.neighbors.append(graph[neighbor])
        
        return graph[node]
            