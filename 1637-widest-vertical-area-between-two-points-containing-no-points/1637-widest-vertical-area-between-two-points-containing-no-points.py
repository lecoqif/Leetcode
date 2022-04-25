class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        
        maxWidth = 0
        
        for i, val in enumerate(points[:-1]):
            maxWidth = max(maxWidth, points[i + 1][0] - val[0])
        
        return maxWidth