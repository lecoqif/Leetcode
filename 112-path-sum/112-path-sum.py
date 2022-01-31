# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        q = deque()
        
        q.append((root, 0))
        
        while len(q) != 0:
            node, val = q.popleft()
            
            val += node.val
            
            if node.right is None and node.left is None and val == targetSum:
                return True
            
            if node.left:
                q.append((node.left, val))
            
            if node.right:
                q.append((node.right, val))
        
        return False
            
        
        
        
        
        