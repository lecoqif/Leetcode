from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        
        for dest, src in prerequisites:
            in_degree[dest] += 1
            graph[src].append(dest)
        
        q = deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        ret = []
        
        while q:
            curr = q.popleft()
            ret.append(curr)
            
            for neigh in graph[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
        
        return ret if len(ret) == numCourses else []
            
        
        
        