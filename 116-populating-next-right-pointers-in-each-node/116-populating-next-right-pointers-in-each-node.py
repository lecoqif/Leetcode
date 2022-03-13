"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import defaultdict

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        levels = defaultdict(list)
        
        q = deque([(0, root)])
        
        while len(q) > 0:
            curr_len = len(q)
            
            for i in range(curr_len):
                depth, node = q.popleft()
                
                levels[depth].append(node)
                
                for leaf in [node.left, node.right]:
                    if leaf:
                        q.append((depth + 1, leaf))
                
        for level in levels:
            for i, node in enumerate(levels[level]):
                if i < len(levels[level]) - 1:
                    node.next = levels[level][i + 1]
        
        return root