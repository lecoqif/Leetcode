# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        
        q.append((root, 1))
        
        ret = 0
        
        while len(q) > 0:
            node, depth = q.popleft()
            
            if not node.right and not node.left:
                ret = max(ret, depth)
                continue
            
            if node.right:
                q.append((node.right, depth + 1))
            
            if node.left:
                q.append((node.left, depth + 1))
            
        return ret