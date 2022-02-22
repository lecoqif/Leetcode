class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            
        indegree = {node : 0 for node in range(numCourses)}
        
        for node in graph:
            for dest in graph[node]:
                indegree[dest] += 1
        
        no_incoming_edges = []
        
        for node in indegree:
            if indegree[node] == 0:
                no_incoming_edges.append(node)
        
        ret = []
        
        while len(no_incoming_edges) > 0:
            curr = no_incoming_edges.pop(0)
            ret.append(curr)
            
            for dest in graph[curr]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    no_incoming_edges.append(dest)
        
        if len(ret) == numCourses:
            return True
        
        return False
            
        
        