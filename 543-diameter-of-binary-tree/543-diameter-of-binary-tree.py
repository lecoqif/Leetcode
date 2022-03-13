# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        
        diameter = 0
        
        def dfs(node = root):
            
            if not node:
                return 0
            
            rdepth = dfs(node.right) if node.right else 0
            
            ldepth = dfs(node.left) if node.left else 0
            
            global diameter
            
            diameter = max(diameter, ldepth + rdepth)
            
            return max(rdepth, ldepth) + 1
            
        dfs()
        
        return diameter