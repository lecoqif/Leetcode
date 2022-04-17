class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        
        curr = points[0]
        
        arrows = 1
        
        for i in range(1, len(points)):
            if points[i][0] > curr[1]:
                arrows += 1
                curr = points[i]
        
        return arrows