# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from hashlib import sha256
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def hash_(x):
            S = sha256()
            x = x.encode("utf-8")
            S.update(x)
            return S.hexdigest()
        
        def merkle(node):
            if not node:
                return "#"
            
            l = merkle(node.left)
            r = merkle(node.right)
            node.merkle = hash_(l + str(node.val) + r)
            return node.merkle
        
        merkle(root)
        merkle(subRoot)
        
        def dfs(node):
            if not node:
                return False
            
            return node.merkle == subRoot.merkle or dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        
        
            
            