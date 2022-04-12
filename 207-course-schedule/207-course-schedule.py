from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            incoming[prereq[0]] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if incoming[i] == 0:
                q.append(i)

        ret = []
        
        while q:
            curr = q.popleft()
            ret.append(curr)
            
            for neigh in graph[curr]:
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    q.append(neigh)
        

        return len(ret) == numCourses
            
            
        
        
        
        