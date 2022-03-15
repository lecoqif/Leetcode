# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        
        st = deque([root])
        
        while(len(st) != 0):
            node = st.popleft()
            
            for leaf in [node.left, node.right]:
                if leaf:
                    parents[leaf] = node
                    st.append(leaf)
        
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
        
      
        