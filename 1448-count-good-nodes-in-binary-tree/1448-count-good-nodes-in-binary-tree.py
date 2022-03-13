# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global ret
        ret = 0
        
        def dfs(node = root, curr_max = float('-inf')):
            global ret
            if node.val >= curr_max:
                ret += 1
            
            curr_max = max(node.val, curr_max)
            
            if node.right:
                dfs(node.right, curr_max)
            
            if node.left:
                dfs(node.left, curr_max)
        
        dfs()
        
        return ret
            