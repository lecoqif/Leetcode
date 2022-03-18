# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque()
        
        q.append(root)
        
        ret = []
        
        while len(q) > 0:
            size = len(q)
            
            avg = 0
            n = 0
            
            for i in range(size):
                node = q.popleft()
                
                avg += node.val
                
                n += 1
                
                for leaf in [node.left, node.right]:
                    if leaf:
                        q.append(leaf)
                
            
            ret.append(avg / n)
        
        return ret
                
                