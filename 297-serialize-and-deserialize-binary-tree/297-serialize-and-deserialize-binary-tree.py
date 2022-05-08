# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        stack = []
        
        stack.append(root)
        
        res = []
        
        while stack:
            curr = stack.pop()
            
            if not curr:
                res.append('#')
                continue
            
            res.append(str(curr.val))
            
            for child in [curr.right, curr.left]:
                stack.append(child)
        
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(',')
        
        count = 0
        
        def dfs() -> TreeNode:
            nonlocal count
            
            if tree[count] == '#':
                count += 1
                return None
            
            root = TreeNode(int(tree[count]))
            
            count += 1
            
            root.left = dfs()
            
            root.right = dfs()
            
            return root
            
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))