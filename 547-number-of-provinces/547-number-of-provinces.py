class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        def dfs(node):
            stack = [node]
            while len(stack) > 0:
                curr = stack.pop()
                vis.add(curr)
                for k in range(len(M[curr])):
                    if k != curr and k not in vis and M[curr][k] == 1:
                        stack.append(k)
            
                
        nodes = list(range(len(M)))
        vis = set()
        prov = 0
        
        for node in nodes:
            if node not in vis:
                prov += 1
                dfs(node)
        
        return prov
        