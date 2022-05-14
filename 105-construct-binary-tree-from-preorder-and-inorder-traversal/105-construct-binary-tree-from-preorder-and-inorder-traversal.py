# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        indexes = {node : i for i, node in enumerate(inorder)}
        
        idx = 0
        
        def dfs(left: int, right: int):
            nonlocal idx
            if right < left: return
            
            val = preorder[idx]
            
            node = TreeNode(val)
            idx += 1
            
            node.left = dfs(left, indexes[val] - 1)
            node.right = dfs(indexes[val] + 1, right)
            
            return node
        
        
        root = dfs(0, len(inorder) - 1)
        
        return root
  
        