# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        
        st = [root]
        
        while(len(st) != 0):
            node = st.pop(0)
            if node.left:
                parents[node.left] = node
                st.append(node.left)
            
            if node.right:
                parents[node.right] = node
                st.append(node.right)
        
        ps = set()
        
        curr = p
        
        while(curr):
            ps.add(curr)
            curr = parents[curr]
        
        curr = q
        
        while(curr):
            if curr in ps:
                return curr
            curr = parents[curr]
        
      
        