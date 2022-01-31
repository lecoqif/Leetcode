# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def check(node, lower=None, upper=None):
            if node is None:
                return True
            
            if lower is not None and node.val <= lower:
                return False
            
            if upper is not None and node.val >= upper:
                return False
            
            return check(node.left, lower, node.val) and check(node.right, node.val, upper)

        return check(root)