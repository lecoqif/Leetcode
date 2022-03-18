# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        levels = []
        
        q = deque()
        
        q.append(root)
        
        while len(q) > 0:
            size = len(q)
            
            level = []
            
            for i in range(size):
                node = q.popleft()
                
                level.append(node.val)
                
                for leaf in [node.left, node.right]:
                    if leaf:
                        q.append(leaf)
            
            levels.append(level)
        
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i] = levels[i][::-1]
        
        return levels
                
        
        