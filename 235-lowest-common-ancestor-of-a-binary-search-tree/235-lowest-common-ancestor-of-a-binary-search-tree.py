# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        a = p if p.val <= q.val else q
        
        b = q if p.val <= q.val else p
        
        if a.val <= root.val and b.val >= root.val:
            return root
        
        if a.val < root.val and b.val < root.val:
            return self.lowestCommonAncestor(root.left, a, b)
        
        if a.val > root.val and b.val > root.val:
            return self.lowestCommonAncestor(root.right, a, b)