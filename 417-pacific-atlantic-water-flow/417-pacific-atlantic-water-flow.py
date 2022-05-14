class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pacific_start, atlantic_start = set(), set()
        
        for i in range(ROWS):
            pacific_start.add((i, 0))
            atlantic_start.add((i, COLS - 1))
        
        for j in range(COLS):
            pacific_start.add((0, j))
            atlantic_start.add((ROWS - 1, j))
        
        def bfs(start_points):
            
            q = deque(start_points)
            
            while q:
                curr = q.popleft()
                
                dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                
                for way in dirs:
                    newX, newY = curr[0] + way[0], curr[1] + way[1]
                    
                    if not (0 <= newX < ROWS and 0 <= newY < COLS and (newX, newY) not in start_points):
                        continue
                    
                    if heights[newX][newY] >= heights[curr[0]][curr[1]]:
                        start_points.add((newX, newY))
                        q.append((newX, newY))
                
            return start_points
        
        return list(bfs(atlantic_start).intersection(bfs(pacific_start)))
                
            
            
        
            
        