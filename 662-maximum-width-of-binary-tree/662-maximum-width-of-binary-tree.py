# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        q = deque()
        
        q.append((root, 0))
        
        maxWidth = 0
        
        while q:
            size = len(q)
            _, firstIdx = q[0]
            
            for i in range(size):
                curr, idx = q.popleft()
                maxWidth = max(maxWidth, idx - firstIdx + 1)
                
                if curr.left:
                    q.append((curr.left, 2 * idx))
                
                if curr.right:
                    q.append((curr.right, 2 * idx + 1))
            
        return maxWidth
            