# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q_node: 'TreeNode') -> 'TreeNode':
        parents = {}
        
        parents[root] = None
        
        q = deque()
        
        q.append(root)
        
        while q:
            curr = q.popleft()
            
            for child in [curr.left, curr.right]:
                if child:
                    parents[child] = curr
                    q.append(child)
            
        p_ancestors = set()
        
        curr = p
        
        while curr is not None:
            p_ancestors.add(curr.val)
            curr = parents[curr]
        
        curr = q_node
        
        while curr:
            if curr.val in p_ancestors:
                return curr
            
            curr = parents[curr]
        
        return root
        
        
            
            
            

        
        
        