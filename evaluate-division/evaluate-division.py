from collections import defaultdict
from typing import Tuple, List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = set()
        
        # dict: str --> Tuple[str, int]
        graph = defaultdict(list)
        
        for i, equation in enumerate(equations):
            nodes.update(equation)
            graph[equation[0]].append((equation[1], values[i]))
            graph[equation[1]].append((equation[0], 1 / values[i]))
        
        answers = []
        
        for a, b in queries:
            if a not in nodes or b not in nodes:
                answers.append(-1)
                continue
            
            if a == b:
                answers.append(1)
                continue
            
            q = deque()
            
            q.append((a, 1))
            seen = set()
            found = False
            
            while q:
                node, val = q.popleft()
                if node == b:
                    answers.append(val)
                    found = True
                    break
                
                seen.add(node)
                
                for nei, edge in graph[node]:
                    if nei not in seen:
                        q.append((nei, val * edge))
            
            if not found:
                answers.append(-1)
        
        return answers
            
            
            