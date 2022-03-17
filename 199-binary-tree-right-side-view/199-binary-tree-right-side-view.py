# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        q = deque()
        
        q.append(root)
        
        rightside = []
        
        while len(q) > 0:
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                if i == size - 1:
                    rightside.append(node.val)
                
                for leaf in [node.left, node.right]:
                    if leaf:
                        q.append(leaf)
        
        return rightside
        
        