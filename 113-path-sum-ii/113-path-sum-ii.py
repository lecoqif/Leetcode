# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        ret = []
        
        def dfs(node = root, curr_path = [], curr_sum = 0):
            curr_sum += node.val
            curr_path.append(node.val)
            
            if not node.left and not node.right and curr_sum == targetSum:
                ret.append(curr_path)
            
            if node.left:
                dfs(node.left, curr_path[:], curr_sum)
            
            if node.right:
                dfs(node.right, curr_path[:], curr_sum)
            

        dfs()
        
        return ret