class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        
        deq = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ret += 1
                    
                    deq.append((i, j))
                    
                    while len(deq) > 0:
                        row, col = deq.popleft()
                        
                        if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
                            continue
                            
                        grid[row][col] = "0"
                        
                        for way in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                            deq.append((row + way[0], col + way[1]))
        
        return ret
                        
                    
                