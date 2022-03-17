"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        
        if not root:
            return root
        
        q.append(root)
        
        while len(q) > 0:
            size = len(q)
            
            for i in range(size):
                
                curr = q.popleft()
                
                if i != size - 1:
                    curr.next = q[0]
                
                for leaf in [curr.left, curr.right]:
                    if leaf:
                        q.append(leaf)
        
        return root
        
        