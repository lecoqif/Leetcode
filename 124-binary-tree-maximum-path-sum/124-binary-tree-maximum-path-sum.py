# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ret = float('-inf')
        
        self.dfs(root)
        
        return self.ret
    
    def dfs(self, node) -> int:
        if not node:
            return 0
        
        leftSum, rightSum = max(0, self.dfs(node.left)), max(0, self.dfs(node.right))
        
        self.ret = max(self.ret, leftSum + rightSum + node.val)
        
        return node.val + max(leftSum, rightSum)