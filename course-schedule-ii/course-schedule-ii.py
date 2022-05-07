class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        topOrder = []
        
        while q:
            curr = q.popleft()
            topOrder.append(curr)
            
            for nei in graph[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return topOrder if len(topOrder) == numCourses else []