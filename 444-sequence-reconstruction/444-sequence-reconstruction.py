class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        
        for sequence in sequences:
            for i in range(len(sequence) - 1):
                in_degree[sequence[i + 1]] += 1
                graph[sequence[i]].append(sequence[i + 1])
        
        q = deque()
        
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                q.append(i)
        
        
        ret = []
        
        while q:

            if len(q) > 1:
                return False
            
            curr = q.popleft()
            ret.append(curr)
            
            for neigh in graph[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
        

        print(ret)
        return ret == nums
                
            