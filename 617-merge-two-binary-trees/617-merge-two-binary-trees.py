# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        
        if t1 and not t2 or t2 and not t1:
            return t1 if t1 is not None else t2
        
        node = TreeNode(t1.val + t2.val)
        
        node.right = self.mergeTrees(t1.right, t2.right)
        
        node.left = self.mergeTrees(t1.left, t2.left)
        
        return node
        