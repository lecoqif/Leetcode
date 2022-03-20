# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and not subRoot or not root and subRoot:
            return False
        
        q = deque()
        
        q.append(root)
        
        while len(q) > 0:
            node = q.popleft()
            
            if node.val == subRoot.val and self.check(node, subRoot):
                return True
            
            for leaf in [node.left, node.right]:
                if leaf:
                    q.append(leaf)
        
        return False
    
    def check(self, node, subRoot):
        if not node and not subRoot:
            return True
        
        if node and not subRoot or not node and subRoot:
            return False
        
        if node.val != subRoot.val:
            return False
        
        return self.check(node.left, subRoot.left) and self.check(node.right, subRoot.right)
            