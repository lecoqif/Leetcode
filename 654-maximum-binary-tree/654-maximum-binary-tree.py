# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_val = max(nums)
        
        idx_max_val = nums.index(max_val)
        
        root = TreeNode(max_val)
        
        root.left = self.constructMaximumBinaryTree(nums[0:idx_max_val])
        
        root.right = self.constructMaximumBinaryTree(nums[idx_max_val + 1:])
        
        return root