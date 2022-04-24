# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        stack = []
        
        curr = root
        
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            
            else:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                
                curr = node.right
        
        