# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        q = deque()
        
        if root:
            q.append(root)
        
        while len(q) > 0:
            currLen = len(q)
            
            level = []
            
            for i in range(currLen):
                node = q.popleft()
                level.append(node.val)
                
                for leaf in [node.left, node.right]:
                    if leaf:
                        q.append(leaf)
            
            levels.append(level)
        
        return levels[::-1]
                
            
            