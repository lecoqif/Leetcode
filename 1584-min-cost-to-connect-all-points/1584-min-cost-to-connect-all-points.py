class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        in_mst = [False] * n
        
        weights = [float('inf')] * n
        
        edges = 0
        
        weights[0] = 0
        
        ret = 0
        
        while edges < n:
            curr_min_weight = float('inf')
            min_node = -1
            
            for i, weight in enumerate(weights):
                if weight < curr_min_weight and not in_mst[i]:
                    curr_min_weight = weight
                    min_node = i
            
            in_mst[min_node] = True
            
            ret += curr_min_weight
            
            for i, weight in enumerate(weights):
                new_weight = abs(points[min_node][0] - points[i][0]) + abs(points[min_node][1] - points[i][1])
                if new_weight < weight and not in_mst[i]:
                    weights[i] = new_weight
            
            edges += 1
        
        return ret
            
            