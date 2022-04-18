# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parents = {}
        
        def populate_parents(node: TreeNode, parent: TreeNode) -> None:
            if not node:
                return
            
            parents[node] = parent
            populate_parents(node.left, node)
            populate_parents(node.right, node)
        
        populate_parents(root, None)
        
        seen = set()
        
        q = deque()
        
        q.append((target, 0))
        
        res = []
        
        while q:
            curr, dist = q.popleft()
            seen.add(curr.val)
            if dist == K:
                res.append(curr.val)
                continue
            
            for neigh in [parents[curr], curr.left, curr.right]:
                if neigh and neigh.val not in seen:
                    q.append((neigh, dist + 1))
        
        return res
                