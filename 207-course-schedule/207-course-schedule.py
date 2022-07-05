class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for src, dst in prerequisites:
            graph[src].append(dst)
            in_degree[dst] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            curr = q.popleft()
            
            count += 1
            
            in_degree[curr] -= 1
            
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses
        
            
        
            