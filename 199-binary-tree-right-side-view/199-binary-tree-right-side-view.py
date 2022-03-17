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
        
        levels = []
        
        q = deque([(root, 0)])
        
        while len(q) > 0:
            node, depth = q.popleft()
            
            if len(levels) == depth:
                levels.append([])
                
            levels[depth].append(node.val)
            
            for leaf in [node.left, node.right]:
                if leaf:
                    q.append((leaf, depth + 1))
        
        ret = [level[-1] for level in levels]
        
        return ret
        
        